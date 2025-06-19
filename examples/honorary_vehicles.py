#!/usr/bin/env python3
"""
Honorary vehicle generation examples
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from otherides_generator import OtheridesAssetGenerator

def main():
    # Initialize generator
    generator = OtheridesAssetGenerator()
    
    print("🏆 OTHERIDES Honorary Vehicle Examples")
    print("="*45)
    
    # Example 1: Garga tribute (like the original)
    print("\n1. Creating Garga tribute vehicle...")
    garga_vehicle = generator.create_honorary_vehicle(
        honoree_name="Garga",
        honoree_org="Yuga Labs",
        custom_style="rough_cool_tattoo",
        custom_traits=[
            "leopard_skin_pattern",
            "tattoo_body_art", 
            "grill_smirk",
            "dual_headlight_eyes"
        ]
    )
    
    if garga_vehicle:
        print(f"✅ Created: {garga_vehicle['metadata']['variant']}")
        print(f"   File: {garga_vehicle['file_name']}")
        print(f"   Honorary: {garga_vehicle['metadata'].get('honorary', 'N/A')}")
    
    # Example 2: Custom honorary for another figure
    print("\n2. Creating custom honorary vehicle...")
    custom_vehicle = generator.create_honorary_vehicle(
        honoree_name="Satoshi",
        honoree_org="Bitcoin",
        custom_style="sleek_corporate",
        custom_traits=[
            "chrome_finish",
            "blockchain_patterns",
            "led_accents",
            "digital_displays"
        ]
    )
    
    if custom_vehicle:
        print(f"✅ Created: {custom_vehicle['metadata']['variant']}")
        print(f"   Style: {custom_vehicle['metadata']['style']}")
        print(f"   Traits: {', '.join(custom_vehicle['metadata']['traits'][:3])}...")
    
    # Example 3: Community tribute
    print("\n3. Creating community tribute vehicle...")
    community_vehicle = generator.create_honorary_vehicle(
        honoree_name="Apes",
        honoree_org="BAYC Community",
        custom_style="organic_bio",
        custom_traits=[
            "banana_accents",
            "jungle_camo",
            "vine_details",
            "tribal_markings"
        ]
    )
    
    if community_vehicle:
        print(f"✅ Created: {community_vehicle['metadata']['variant']}")
        print(f"   Biome: {community_vehicle['metadata']['biome']}")
        print(f"   Camera: {community_vehicle['metadata']['camera_view']}")
    
    print("\n🎉 Honorary vehicle generation complete!")
    print("🏆 Perfect for special tributes and collaborations.")

if __name__ == "__main__":
    main()