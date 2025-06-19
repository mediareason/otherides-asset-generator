#!/usr/bin/env python3
"""
Utility to view and manage the OTHERIDES vehicle database
"""

import sqlite3
import json
from datetime import datetime
import sys
import os

def view_all_vehicles(db_path="otherides_assets.db"):
    """Display all vehicles in the database"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, image_id, faction, vehicle_type, variant, biome, 
                   style, generation_date, honorary
            FROM otherides_vehicles 
            ORDER BY created_at DESC
        """)
        
        vehicles = cursor.fetchall()
        
        if not vehicles:
            print("💭 No vehicles found in database.")
            return
        
        print(f"📊 OTHERIDES Vehicle Database ({len(vehicles)} vehicles)")
        print("="*80)
        
        for vehicle in vehicles:
            id, image_id, faction, vehicle_type, variant, biome, style, gen_date, honorary = vehicle
            
            print(f"🆔 ID: {id}")
            print(f"   Image ID: {image_id}")
            print(f"   Faction: {faction.title() if faction else 'N/A'}")
            print(f"   Type: {vehicle_type.title() if vehicle_type else 'N/A'}")
            print(f"   Variant: {variant}")
            print(f"   Biome: {biome.title() if biome else 'N/A'}")
            print(f"   Style: {style}")
            if honorary:
                print(f"   🏆 Honorary: {honorary}")
            print(f"   Generated: {gen_date}")
            print()
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    except FileNotFoundError:
        print(f"❌ Database file not found: {db_path}")

def view_faction_stats(db_path="otherides_assets.db"):
    """Display statistics by faction"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT faction, COUNT(*) as count
            FROM otherides_vehicles 
            GROUP BY faction
            ORDER BY count DESC
        """)
        
        stats = cursor.fetchall()
        
        if not stats:
            print("💭 No faction statistics available.")
            return
        
        print("📊 Faction Statistics")
        print("="*30)
        
        total = sum(stat[1] for stat in stats)
        
        for faction, count in stats:
            percentage = (count / total) * 100
            faction_name = faction.replace('_', ' ').title() if faction else 'Unknown'
            print(f"   {faction_name:<15} {count:>3} ({percentage:5.1f}%)")
        
        print(f"\n   Total Vehicles: {total}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")

def view_biome_distribution(db_path="otherides_assets.db"):
    """Display biome distribution"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT biome, COUNT(*) as count
            FROM otherides_vehicles 
            GROUP BY biome
            ORDER BY count DESC
        """)
        
        stats = cursor.fetchall()
        
        if not stats:
            print("💭 No biome statistics available.")
            return
        
        print("🌍 Biome Distribution")
        print("="*30)
        
        for biome, count in stats:
            biome_name = biome.replace('_', ' ').title() if biome else 'Unknown'
            print(f"   {biome_name:<15} {count:>3}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")

def export_metadata(db_path="otherides_assets.db", output_file=None):
    """Export all vehicle metadata to JSON"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM otherides_vehicles ORDER BY created_at DESC")
        vehicles = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        
        if not vehicles:
            print("💭 No vehicles to export.")
            return
        
        # Convert to list of dictionaries
        vehicle_list = []
        for vehicle in vehicles:
            vehicle_dict = dict(zip(columns, vehicle))
            
            # Parse JSON fields
            if vehicle_dict.get('traits'):
                try:
                    vehicle_dict['traits'] = json.loads(vehicle_dict['traits'])
                except json.JSONDecodeError:
                    pass
            
            if vehicle_dict.get('tags'):
                try:
                    vehicle_dict['tags'] = json.loads(vehicle_dict['tags'])
                except json.JSONDecodeError:
                    pass
            
            vehicle_list.append(vehicle_dict)
        
        # Create export data
        export_data = {
            'export_timestamp': datetime.now().isoformat(),
            'total_vehicles': len(vehicle_list),
            'vehicles': vehicle_list
        }
        
        # Determine output filename
        if not output_file:
            output_file = f"otherides_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        # Write to file
        with open(output_file, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        print(f"✅ Exported {len(vehicle_list)} vehicles to {output_file}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    except Exception as e:
        print(f"❌ Export error: {e}")

def main():
    """Main CLI interface"""
    if len(sys.argv) < 2:
        print("📊 OTHERIDES Database Viewer")
        print("="*35)
        print("Usage: python database_viewer.py <command> [options]")
        print("\nCommands:")
        print("  all        - View all vehicles")
        print("  factions   - View faction statistics")
        print("  biomes     - View biome distribution")
        print("  export     - Export all data to JSON")
        print("\nOptions:")
        print("  --db <path>     - Specify database path (default: otherides_assets.db)")
        print("  --output <file> - Specify output file for export")
        return
    
    command = sys.argv[1]
    db_path = "otherides_assets.db"
    output_file = None
    
    # Parse options
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--db" and i + 1 < len(sys.argv):
            db_path = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--output" and i + 1 < len(sys.argv):
            output_file = sys.argv[i + 1]
            i += 2
        else:
            i += 1
    
    # Execute command
    if command == "all":
        view_all_vehicles(db_path)
    elif command == "factions":
        view_faction_stats(db_path)
    elif command == "biomes":
        view_biome_distribution(db_path)
    elif command == "export":
        export_metadata(db_path, output_file)
    else:
        print(f"❌ Unknown command: {command}")
        print("Use 'all', 'factions', 'biomes', or 'export'")

if __name__ == "__main__":
    main()