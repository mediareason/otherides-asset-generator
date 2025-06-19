# Quick Start Guide

Get up and running with the OTHERIDES Asset Generator in 5 minutes!

## 🚀 Quick Setup

### 1. Clone the Repository
```bash
git clone https://github.com/mediareason/otherides-asset-generator.git
cd otherides-asset-generator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment
```bash
# Copy the environment template
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=your_key_here
```

### 4. Test the Generator
```bash
# Run basic example
python examples/basic_generation.py

# Or run the main generator
python otherides_generator.py
```

## ✨ First Generation Examples

### Generate a Random Vehicle
```python
from otherides_generator import OtheridesAssetGenerator

generator = OtheridesAssetGenerator()
vehicle = generator.generate_otherides_vehicle()

print(f"Created: {vehicle['variant']}")
print(f"Faction: {vehicle['faction']}")
print(f"Biome: {vehicle['biome']}")
```

### Create an Honorary Vehicle
```python
# Like the famous Garga Leopard Tattoo Car
garga = generator.create_honorary_vehicle(
    honoree_name="Garga",
    honoree_org="Yuga Labs",
    custom_style="rough_cool_tattoo",
    custom_traits=["leopard_skin_pattern", "tattoo_body_art"]
)
```

### Generate Faction-Specific Vehicles
```python
# Amalfi Noble Planners in Crystal biome
amalfi_racer = generator.generate_otherides_vehicle(
    faction='amalfi',
    biome='crystal', 
    style='noble_refined',
    vehicle_type='speedster'
)

# Apostates Chaotic Zealots in Chaos biome
chaos_destroyer = generator.generate_otherides_vehicle(
    faction='apostates',
    biome='chaos',
    style='mystical_ritual',
    vehicle_type='destroyer'  
)
```

## 🎯 Key Features to Try

### 1. **All 6 Real Factions**
- `amalfi` - Noble Planners with crystalline luxury
- `raven_coats` - Stealth Tacticians with tactical armor  
- `united_welders` - Industrial Builders with raw steel
- `scion` - Corporate Killers with neon precision
- `kerr_org` - Naturebound Dualists with organic tech
- `apostates` - Chaotic Zealots with ritual madness

### 2. **29 Otherside Biomes**
- Common: `swamp`, `glacier`, `molten`, `jungle`
- Rare: `crystal`, `shadow`, `bone`, `obsidian`  
- Legendary: `chaos` (0.11% rarity in Otherside)

### 3. **6 Aesthetic Styles**
- `rough_cool_tattoo` - Street aesthetic with ink patterns
- `sleek_corporate` - Clean professional design
- `brutalist_industrial` - Raw mechanical brutalism
- `organic_bio` - Living symbiotic technology
- `mystical_ritual` - Arcane magical elements
- `noble_refined` - Elegant luxury craftsmanship

### 4. **7 Vehicle Types**
- `speedster` - Ultra-fast single-seat racers
- `bruiser` - Heavy multi-terrain assault vehicles
- `glider` - Anti-gravity hovering vehicles
- `phantom` - Stealth cloaking vehicles
- `destroyer` - Weapon-laden combat racers
- `explorer` - Long-range expedition vehicles
- `buggy` - All-terrain off-road racers

## 📁 Example Scripts

Run these to see different capabilities:

```bash
# Basic generation examples
python examples/basic_generation.py

# Honorary vehicle examples  
python examples/honorary_vehicles.py

# Showcase all factions
python examples/faction_showcase.py
```

## 🗄️ Database Management

```bash
# View all generated vehicles
python utils/database_viewer.py all

# See faction statistics
python utils/database_viewer.py factions

# Export all data
python utils/database_viewer.py export
```

## 🔧 Optional: Google Drive Integration

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Enable Google Drive API
3. Download credentials as `credentials.json`
4. First run will open browser for OAuth

## 🎨 Output Structure

Generated vehicles follow authentic OTHERIDES format:

```json
{
  "image_id": "amalfi_crystal_noble_speedster_v01",
  "faction": "Amalfi", 
  "vehicle_type": "Speedster",
  "variant": "Crystal Noble Speedster",
  "biome": "Crystal",
  "style": "Noble Refined",
  "traits": ["crystalline_body", "noble_design", "hover_tech"],
  "camera_view": "Front 3/4",
  "lighting": "Bright studio lighting"
}
```

## 🆘 Troubleshooting

**OpenAI API Error?**
- Check your API key in `.env`
- Ensure you have credits in your OpenAI account

**No Google Drive Upload?**
- Drive integration is optional
- Generator works fine without it
- Images still save metadata to database

**Import Errors?**
- Run `pip install -r requirements.txt`
- Check Python version (3.8+ required)

## 🎯 Next Steps

1. **Generate your first collection** with `python otherides_generator.py`
2. **Explore faction lore** in `data/otherides_factions.json`
3. **Customize prompts** by modifying the generator
4. **Build workflows** for your 3D pipeline integration
5. **Create honorary vehicles** for special collaborations

---

🏁 **Ready to create the next generation of OTHERIDES vehicles!**

Check out the [full documentation](README.md) for advanced features and customization options.
