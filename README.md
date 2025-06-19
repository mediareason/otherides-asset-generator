# OTHERIDES Asset Generator

AI-powered vehicle generator for the OTHERIDES NFT collection with authentic faction lore, real Otherside metaverse biomes, and 3D pipeline integration.

## Features

🏁 **Authentic OTHERIDES Lore**
- 6 real factions: Amalfi, Raven Coats, United Welders, Scion, Kerr Org, Apostates
- Honorary tribute vehicles (like the Garga Leopard Tattoo Car)
- Faction-specific materials, aesthetics, and vehicle themes

🌍 **Real Otherside Biomes**
- All 29 official Otherside metaverse environments
- From Biogenic Swamp to Chaos biome
- Authentic environmental descriptions

📊 **NFT-Ready Metadata**
- OpenSea-compatible trait structure
- Organized file naming and folder structure
- Database tracking for collection management

🎨 **3D Pipeline Integration**
- High-quality concept art generation
- Multiple camera angles and lighting setups
- Material property analysis for 3D workflows

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. API Keys

Create a `.env` file with your API keys:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Google Drive Integration (Optional)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google Drive API
4. Create credentials (OAuth 2.0)
5. Download as `credentials.json` in project root

## Usage

### Basic Vehicle Generation

```python
from otherides_generator import OtheridesAssetGenerator

generator = OtheridesAssetGenerator()

# Generate a faction vehicle
vehicle = generator.generate_otherides_vehicle(
    faction='amalfi',      # Noble Planners
    biome='crystal',       # Real Otherside biome
    style='noble_refined'
)

print(f"Generated: {vehicle['variant']}")
```

### Honorary Vehicles

```python
# Create an honorary vehicle like the Garga example
honor_vehicle = generator.create_honorary_vehicle(
    honoree_name="Garga",
    honoree_org="Yuga Labs",
    custom_style="rough_cool_tattoo",
    custom_traits=["leopard_skin_pattern", "tattoo_body_art"]
)
```

### Batch Generation

```python
# Run the main example
python otherides_generator.py
```

## Faction Guide

### Amalfi (Noble Planners)
- **Style**: Streamlined and sculpted
- **Materials**: Crystalline bodywork, gold trim, pearl enamel
- **Themes**: Regal racers, hover-inspired tech, precision over power
- **Influences**: The Culture, Dune, Blade Runner corporate elite

### Raven Coats (Stealth Tacticians)
- **Style**: Asymmetrical and agile
- **Materials**: Matte black plating, bioluminescent accents, tactical armor
- **Themes**: Stealth buggies, adaptive racers, mist-cloaked muscle
- **Influences**: Firefly, rogue archetypes, Deadfire

### United Welders (Industrial Builders)
- **Style**: Brutalist and practical
- **Materials**: Riveted iron, patchwork armor, burnt metal
- **Themes**: Bolt-armored muscle, grinder rigs, forged battle cars
- **Influences**: The Expanse, Mad Max, Arcane (Zaun)

### Scion (Corporate Killers)
- **Style**: Sleek and angular
- **Materials**: Carbon fiber, reflective casings, glasslike panels
- **Themes**: Stealth-tech racers, smartframe muscle, electric predators
- **Influences**: Cyberpunk 2077, Neuromancer, corporate hypercars

### Kerr Org (Naturebound Dualists)
- **Style**: Organic and living
- **Materials**: Bark plating, knotted vines, dino-scale textures
- **Themes**: Living buggies, biomechs, symbiotic racers
- **Influences**: Neverending Story, Willow, eco-warriors
- **Subfactions**: Protectors, Warlike Cultivars

### Apostates (Chaotic Zealots)
- **Style**: Jagged and chaotic
- **Materials**: Rusted steel, bones, charred surfaces
- **Themes**: Skull-rigged drag cars, molten war buggies, ritual machines
- **Influences**: Warhammer 40K, Reavers, Mobius-style apocalypse

## Otherside Biomes

The system includes all 29 official Otherside metaverse environments:

**Common**: Swamp, Glacier, Barrens, Molten, Thornwood, Shards, Biolum, Sands, Ruins

**Uncommon**: Sulfuric Water, Wastelands, Mystic, Weldan, Spiers, Malva, Crimson

**Rare**: Jungle, Plague, Bone, Crystal, Sky, Shadow, Mycelium, Obsidian

**Ultra Rare**: Silt, Glitter, Botanical, Acid

**Legendary**: Chaos (0.11% rarity)

## Output Structure

Generated vehicles follow the authentic OTHERIDES metadata format:

```json
{
  "image_id": "amalfi_crystal_noble_speedster_v01",
  "faction": "Amalfi",
  "vehicle_type": "Speedster",
  "variant": "Crystal Noble Speedster",
  "traits": ["crystalline_body", "noble_design", "hover_tech"],
  "biome": "Crystal",
  "style": "Noble Refined",
  "camera_view": "Front 3/4",
  "lighting": "Bright studio lighting",
  "mood": "Dynamic racing spirit"
}
```

## File Organization

```
Otherides_Moodboards/
├── Honoraries/
│   └── honorary_garga_leopard_tattoo_car_v01.png
├── Genesis_Alpha_Collection/
│   ├── amalfi_crystal_noble_speedster_v01.png
│   ├── raven_coats_shadow_stealth_phantom_v01.png
│   └── ...
└── Database/
    └── otherides_assets.db
```

## 3D Pipeline Integration

Generated vehicles include metadata optimized for 3D workflows:

- **Material properties**: Surface analysis for PBR workflows
- **Color palettes**: Dominant colors for material creation
- **Camera angles**: Multiple views for 3D reference
- **Lighting data**: Professional lighting setups
- **Export formats**: JSON/YAML for 3D applications

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is for educational and development purposes. OTHERIDES is a trademark of Yuga Labs.

## Support

For issues and questions:
- Create an issue on GitHub
- Check existing documentation
- Review faction data in `data/otherides_factions.json`

---

🏁 **Ready to generate the next evolution of OTHERIDES vehicles!**
