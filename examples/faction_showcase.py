#!/usr/bin/env python3
"""
Faction showcase - generate one vehicle from each faction
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from otherides_generator import OtheridesAssetGenerator

def main():
    generator = OtheridesAssetGenerator()
    
    print("🏁 OTHERIDES Faction Showcase")
    print("="*40)
    print("Generating one vehicle from each faction...\n")
    
    # Faction-specific configurations
    faction_configs = {
        'amalfi': {
            'biome': 'crystal',
            'style': 'noble_refined',
            'vehicle_type': 'speedster',
            'description': 'Noble Planners - Precision over power'
        },
        'raven_coats': {
            'biome': 'shadow',
            'style': 'brutalist_industrial',
            'vehicle_type': 'phantom',
            'description': 'Stealth Tacticians - Masters of deception'
        },
        'united_welders': {
            'biome': 'ruins',
            'style': 'brutalist_industrial',
            'vehicle_type': 'bruiser',
            'description': 'Industrial Builders - Raw steel rebellion'
        },
        'scion': {
            'biome': 'biolum',
            'style': 'sleek_corporate',
            'vehicle_type': 'speedster',
            'description': 'Corporate Killers - Neon speed precision'
        },
        'kerr_org': {
            'biome': 'jungle',
            'style': 'organic_bio',
            'vehicle_type': 'explorer',
            'description': 'Naturebound Dualists - Living symbiosis'
        },
        'apostates': {
            'biome': 'chaos',
            'style': 'mystical_ritual',
            'vehicle_type': 'destroyer',
            'description': 'Chaotic Zealots - Ritual madness'
        }
    }
    
    generated_vehicles = []
    
    for faction, config in faction_configs.items():
        print(f"\n🏠 {faction.replace('_', ' ').title()} Faction")
        print(f"   {config['description']}")
        print(f"   Generating {config['vehicle_type']} in {config['biome']} biome...")
        
        vehicle_data = generator.generate_otherides_vehicle(
            faction=faction,
            biome=config['biome'],
            style=config['style'],
            vehicle_type=config['vehicle_type']
        )
        
        if vehicle_data:
            print(f"   ✅ {vehicle_data['variant']}")
            print(f"      Style: {vehicle_data['style']}")
            print(f"      Camera: {vehicle_data['camera_view']}")
            print(f"      Traits: {', '.join(vehicle_data['traits'][:3])}...")
            
            # Save the vehicle
            saved_vehicle = generator._save_otherides_vehicle(
                vehicle_data,
                "Faction_Showcase_Collection"
            )
            
            if saved_vehicle:
                generated_vehicles.append(saved_vehicle)
                print(f"      💾 Saved as: {saved_vehicle['file_name']}")
        else:
            print(f"   ❌ Failed to generate {faction} vehicle")
    
    print(f"\n\n🎆 Faction Showcase Complete!")
    print(f"📊 Generated {len(generated_vehicles)}/6 faction vehicles")
    print(f"🌍 Showcasing the diversity of OTHERIDES factions")
    print(f"🎨 Each vehicle reflects its faction's unique aesthetic")
    
    # Display summary
    print(f"\n📄 Vehicle Summary:")
    for vehicle in generated_vehicles:
        faction = vehicle['metadata']['faction']
        variant = vehicle['metadata']['variant']
        biome = vehicle['metadata']['biome']
        print(f"   • {faction}: {variant} ({biome})")

if __name__ == "__main__":
    main()