#!/usr/bin/env python3
"""
Basic OTHERIDES vehicle generation example
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from otherides_generator import OtheridesAssetGenerator

def main():
    # Initialize generator
    generator = OtheridesAssetGenerator()
    
    print("🏁 OTHERIDES Basic Generation Example")
    print("="*40)
    
    # Example 1: Generate random vehicle
    print("\n1. Generating random vehicle...")
    random_vehicle = generator.generate_otherides_vehicle()
    
    if random_vehicle:
        print(f"✅ Created: {random_vehicle['variant']}")
        print(f"   Faction: {random_vehicle['faction'].title()}")
        print(f"   Biome: {random_vehicle['biome'].title()}")
        print(f"   Style: {random_vehicle['style']}")
    
    # Example 2: Generate specific faction vehicle
    print("\n2. Generating Amalfi vehicle in Crystal biome...")
    amalfi_vehicle = generator.generate_otherides_vehicle(
        faction='amalfi',
        biome='crystal',
        style='noble_refined',
        vehicle_type='speedster'
    )
    
    if amalfi_vehicle:
        print(f"✅ Created: {amalfi_vehicle['variant']}")
        print(f"   Traits: {', '.join(amalfi_vehicle['traits'][:3])}...")
        print(f"   Camera: {amalfi_vehicle['camera_view']}")
        print(f"   Lighting: {amalfi_vehicle['lighting']}")
    
    # Example 3: Generate Apostates chaos vehicle
    print("\n3. Generating Apostates vehicle in Chaos biome...")
    chaos_vehicle = generator.generate_otherides_vehicle(
        faction='apostates',
        biome='chaos',
        style='mystical_ritual',
        vehicle_type='destroyer'
    )
    
    if chaos_vehicle:
        print(f"✅ Created: {chaos_vehicle['variant']}")
        print(f"   ID: {chaos_vehicle['image_id']}")
        print(f"   Tags: {', '.join(chaos_vehicle['tags'])}")
    
    print("\n🎉 Basic generation complete!")
    print("💡 Try running the main generator for full collections.")

if __name__ == "__main__":
    main()