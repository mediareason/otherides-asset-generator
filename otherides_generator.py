#!/usr/bin/env python3
"""
OTHERIDES Asset Generator

AI-powered vehicle generator for the OTHERIDES NFT collection with authentic 
faction lore, real Otherside metaverse biomes, and 3D pipeline integration.
"""

import openai
import os
import requests
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import io
from datetime import datetime
import json
import hashlib
import sqlite3
from typing import List, Dict, Optional, Tuple
import random
from pathlib import Path

class OtheridesAssetGenerator:
    def __init__(self, db_path="otherides_assets.db"):
        self.openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.drive_service = self._setup_google_drive()
        self.db_path = db_path
        self._setup_database()
        
        # Load faction data from JSON file
        self.racing_factions = self._load_faction_data()
        
        # Real Otherside biomes (29 environments from the metaverse)
        self.biomes = {
            'swamp': 'Biogenic swamp environment with murky waters and twisted vegetation',
            'glacier': 'Frozen glacier environment with ice formations and snow',
            'barrens': 'Desolate barren landscape with rocky outcroppings',
            'molten': 'Molten lava environment with fire and volcanic activity',
            'thornwood': 'Dark thornwood forest with twisted spiky trees',
            'shards': 'Crystalline shard environment with jagged crystal formations',
            'biolum': 'Bioluminescent environment with glowing organic structures',
            'sands': 'Desert sands environment with dunes and arid landscape',
            'ruins': 'Ancient ruins environment with crumbling structures',
            'sulfuric_water': 'Sulfuric water environment with toxic pools',
            'wastelands': 'Post-apocalyptic wasteland with debris and decay',
            'mystic': 'Mystical environment with magical energies and ethereal mists',
            'weldan': 'Weldan metallic environment with industrial structures',
            'spiers': 'Towering spiers environment with tall needle-like formations',
            'malva': 'Malva environment with purple-hued alien landscapes',
            'crimson': 'Crimson environment with red-tinted terrain and atmosphere',
            'jungle': 'Dense jungle environment with lush tropical vegetation',
            'plague': 'Plague-ridden environment with diseased and corrupted landscape',
            'bone': 'Bone environment filled with skeletal remains and calcium structures',
            'crystal': 'Pure crystal environment with transparent geometric formations',
            'sky': 'Sky environment with floating platforms and aerial landscapes',
            'shadow': 'Shadow environment with dark voids and minimal lighting',
            'mycelium': 'Mycelium environment with fungal networks and spore clouds',
            'obsidian': 'Obsidian environment with black volcanic glass formations',
            'silt': 'Silt environment with fine sediment and muddy terrain',
            'glitter': 'Glitter environment with sparkling, reflective surfaces',
            'botanical': 'Botanical garden environment with diverse plant life',
            'acid': 'Acid environment with corrosive pools and toxic atmosphere',
            'chaos': 'Chaotic environment with reality-bending anomalies and instability',
            # Special honorary biome
            'miami_swamp': 'gray-purple Miami swamp with mist and soft twilight lighting'
        }
        
        self.vehicle_types = {
            'speedster': 'ultra-fast single-seat racer with aerodynamic body',
            'bruiser': 'heavy-duty multi-terrain assault vehicle',
            'glider': 'hovering vehicle with anti-gravity propulsion',
            'phantom': 'stealth vehicle with cloaking capabilities',
            'destroyer': 'weapon-laden combat racer',
            'explorer': 'long-range vehicle built for unknown territories',
            'buggy': 'all-terrain off-road racing vehicle'
        }
        
        # Vehicle aesthetic styles
        self.aesthetic_styles = {
            'rough_cool_tattoo': 'Rough Cool / Tattoo Aesthetic',
            'sleek_corporate': 'Sleek Corporate',
            'brutalist_industrial': 'Brutalist Industrial',
            'organic_bio': 'Organic Bio-Tech',
            'mystical_ritual': 'Mystical Ritual',
            'noble_refined': 'Noble Refined'
        }
        
        # Camera views and lighting
        self.camera_views = ['Front 3/4', 'Side Profile', 'Rear 3/4', 'Top Down', 'Close Detail']
        self.lighting_setups = [
            'Moody purple-gray haze',
            'Bright studio lighting', 
            'Dramatic sunset',
            'Neon night glow',
            'Soft natural light'
        ]
        
    def _load_faction_data(self):
        """Load faction data from JSON file"""
        try:
            faction_file = Path(__file__).parent / 'data' / 'otherides_factions.json'
            with open(faction_file, 'r') as f:
                faction_list = json.load(f)
            
            # Convert list to dict format
            factions = {}
            for faction in faction_list:
                key = faction['name'].lower().replace(' ', '_')
                factions[key] = {
                    'archetype': faction['archetype'],
                    'keywords': faction['keywords'],
                    'materials': faction['design_traits']['materials'],
                    'style': faction['design_traits']['style'],
                    'aesthetic_influences': faction['design_traits']['aesthetic_influences'],
                    'vehicle_themes': faction['vehicle_themes']
                }
                
                # Handle Kerr Org subfactions
                if 'subfactions' in faction:
                    factions[key]['subfactions'] = {
                        sub['name'].lower().replace(' ', '_'): f"{sub['focus']}, {sub['aesthetic']}"
                        for sub in faction['subfactions']
                    }
            
            # Add Honorary faction
            factions['honorary'] = {
                'archetype': 'Tribute Vehicles',
                'keywords': ['tribute', 'legacy', 'special', 'commemorative', 'unique'],
                'materials': ['custom themed bodywork', 'signature patterns', 'personalized details'],
                'style': 'varies by honoree',
                'aesthetic_influences': ['personal style of honoree'],
                'vehicle_themes': ['custom tribute vehicles', 'signature aesthetics', 'legacy racers']
            }
            
            return factions
            
        except FileNotFoundError:
            print("Warning: Faction data file not found. Using fallback data.")
            return self._get_fallback_factions()
    
    def _get_fallback_factions(self):
        """Fallback faction data if JSON file not found"""
        return {
            'amalfi': {
                'archetype': 'Noble Planners',
                'keywords': ['luxury', 'elegance', 'long-term vision', 'refinement', 'high society'],
                'materials': ['crystalline bodywork', 'gold trim', 'pearl enamel'],
                'style': 'streamlined and sculpted',
                'aesthetic_influences': ['The Culture', 'Dune', 'Blade Runner corporate elite'],
                'vehicle_themes': ['regal racers', 'hover-inspired tech', 'precision over power']
            },
            'raven_coats': {
                'archetype': 'Stealth Tacticians',
                'keywords': ['secrecy', 'strategy', 'trickery', 'ambush', 'deception'],
                'materials': ['matte black plating', 'bioluminescent accents', 'tactical armor'],
                'style': 'asymmetrical and agile',
                'aesthetic_influences': ['Firefly', 'rogue archetypes', 'Deadfire'],
                'vehicle_themes': ['stealth buggies', 'adaptive racers', 'mist-cloaked muscle']
            }
        }
    
    def _setup_google_drive(self):
        """Setup Google Drive API authentication"""
        SCOPES = ['https://www.googleapis.com/auth/drive.file']
        creds = None
        
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if os.path.exists('credentials.json'):
                    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                else:
                    print("Warning: Google Drive credentials not found. Drive upload will be disabled.")
                    return None
            
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        
        try:
            return build('drive', 'v3', credentials=creds)
        except Exception as e:
            print(f"Warning: Could not initialize Google Drive service: {e}")
            return None
    
    def _setup_database(self):
        """Database schema for OTHERIDES NFT collection"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS otherides_vehicles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_id TEXT UNIQUE,
                token_id INTEGER,
                vehicle_name TEXT,
                faction TEXT,
                vehicle_type TEXT,
                variant TEXT,
                traits TEXT,
                biome TEXT,
                style TEXT,
                camera_view TEXT,
                lighting TEXT,
                mood TEXT,
                honorary TEXT,
                creator TEXT DEFAULT 'AI_Generator',
                generation_date TEXT,
                source_prompt TEXT,
                tags TEXT,
                file_name TEXT,
                file_path TEXT,
                drive_id TEXT,
                drive_link TEXT,
                created_at TIMESTAMP,
                collection_batch TEXT,
                image_hash TEXT,
                minted BOOLEAN DEFAULT FALSE,
                opensea_ready BOOLEAN DEFAULT FALSE
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def generate_otherides_vehicle(self, faction=None, vehicle_type=None, biome=None, 
                                 style=None, honorary=None, custom_traits=None, variant=None):
        """Generate a vehicle matching real OTHERIDES structure"""
        
        # Random selection if not specified
        if not faction:
            faction = random.choice(list(self.racing_factions.keys()))
        if not vehicle_type:
            vehicle_type = random.choice(list(self.vehicle_types.keys()))
        if not biome:
            biome = random.choice(list(self.biomes.keys()))
        if not style:
            style = random.choice(list(self.aesthetic_styles.keys()))
        
        faction_data = self.racing_factions[faction]
        vehicle_desc = self.vehicle_types[vehicle_type]
        biome_desc = self.biomes[biome]
        style_desc = self.aesthetic_styles[style]
        
        # Generate variant name if not provided
        if not variant:
            variant = self._generate_variant_name(faction, vehicle_type, style)
        
        # Generate image ID
        image_id = self._generate_image_id(faction, variant)
        
        # Select camera view and lighting
        camera_view = random.choice(self.camera_views)
        lighting = random.choice(self.lighting_setups)
        
        # Create comprehensive prompt
        if faction == 'honorary' and honorary:
            enhanced_prompt = f"""
            A tribute vehicle honoring {honorary}, designed as a {vehicle_desc} with {style_desc}.
            
            VEHICLE: {variant}
            STYLE: {style_desc}
            BIOME: {biome_desc}
            CAMERA: {camera_view}
            LIGHTING: {lighting}
            
            Key design elements:
            - Custom themed bodywork honoring {honorary}
            - Signature aesthetic elements and patterns
            - High-quality vehicle concept art
            - Professional racing vehicle design
            - Dynamic pose in {biome_desc}
            - Clean background suitable for collection showcase
            
            Art style: Detailed digital concept art, 4K resolution,
            professional game asset quality, clean composition
            """
        else:
            materials = ', '.join(faction_data['materials'])
            keywords = ', '.join(faction_data['keywords'])
            vehicle_theme = random.choice(faction_data['vehicle_themes'])
            
            enhanced_prompt = f"""
            A {style_desc} {vehicle_desc} from the {faction.replace('_', ' ').title()} faction.
            
            VEHICLE: {variant}
            FACTION: {faction_data['archetype']} - {keywords}
            MATERIALS: {materials}
            STYLE: {faction_data['style']}, {style_desc}
            BIOME: {biome_desc}
            CAMERA: {camera_view}  
            LIGHTING: {lighting}
            
            Key design elements:
            - Built with {materials}
            - Embodies {faction_data['archetype']} philosophy
            - {vehicle_theme} aesthetic
            - Racing through {biome_desc}
            - Professional concept art quality
            
            Art style: High-quality digital concept art, detailed vehicle design,
            clean background perfect for NFT collection, 4K resolution
            """
        
        try:
            response = self.openai_client.images.generate(
                model="dall-e-3",
                prompt=enhanced_prompt,
                size="1024x1024",
                quality="hd",
                n=1,
            )
            
            image_url = response.data[0].url
            
            # Generate traits and tags
            traits = self._generate_vehicle_traits(faction, vehicle_type, style, custom_traits)
            tags = self._generate_vehicle_tags(faction, vehicle_type, biome, honorary)
            
            return {
                'image_url': image_url,
                'image_id': image_id,
                'faction': faction,
                'vehicle_type': vehicle_type,
                'variant': variant,
                'traits': traits,
                'biome': biome,
                'style': style_desc,
                'camera_view': camera_view,
                'lighting': lighting,
                'honorary': honorary,
                'prompt': enhanced_prompt,
                'tags': tags
            }
            
        except Exception as e:
            print(f"Error generating OTHERIDES vehicle: {e}")
            return None
    
    def _generate_variant_name(self, faction, vehicle_type, style):
        """Generate variant names matching OTHERIDES style"""
        style_modifiers = {
            'rough_cool_tattoo': ['Tattoo', 'Ink', 'Rough', 'Street'],
            'sleek_corporate': ['Elite', 'Prime', 'Executive', 'Corporate'],
            'brutalist_industrial': ['Heavy', 'Industrial', 'Forge', 'Steel'],
            'organic_bio': ['Bio', 'Living', 'Symbiont', 'Wild'],
            'mystical_ritual': ['Ritual', 'Mystic', 'Sacred', 'Ancient'],
            'noble_refined': ['Noble', 'Pristine', 'Royal', 'Refined']
        }
        
        patterns = ['Leopard', 'Tiger', 'Dragon', 'Phoenix', 'Viper', 'Wolf', 'Eagle', 'Shark']
        elements = ['Fire', 'Ice', 'Lightning', 'Shadow', 'Crystal', 'Steel', 'Bone', 'Gold']
        
        modifier = random.choice(style_modifiers.get(style, ['Custom']))
        pattern = random.choice(patterns)
        
        return f"{pattern} {modifier} {vehicle_type.title()}"
    
    def _generate_image_id(self, faction, variant):
        """Generate image ID matching naming convention"""
        safe_faction = faction.lower().replace(' ', '_')
        safe_variant = variant.lower().replace(' ', '_')
        version = "v01"
        
        if faction == 'honorary':
            return f"honorary_{safe_variant}_{version}"
        else:
            return f"{safe_faction}_{safe_variant}_{version}"
    
    def _generate_vehicle_traits(self, faction, vehicle_type, style, custom_traits):
        """Generate specific visual traits"""
        base_traits = []
        
        # Style-based traits
        if 'tattoo' in style:
            base_traits.extend(['tattoo_body_art', 'ink_patterns', 'street_aesthetic'])
        if 'corporate' in style:
            base_traits.extend(['sleek_panels', 'chrome_accents', 'led_strips'])
        if 'industrial' in style:
            base_traits.extend(['riveted_armor', 'exposed_mechanics', 'rust_weathering'])
        
        # Universal vehicle traits
        base_traits.extend([
            'dual_headlight_eyes',
            'grill_smirk',
            'racing_stance',
            'faction_insignia'
        ])
        
        # Add custom traits
        if custom_traits:
            base_traits.extend(custom_traits)
        
        return base_traits
    
    def _generate_vehicle_tags(self, faction, vehicle_type, biome, honorary):
        """Generate tags for organization and search"""
        tags = [
            faction,
            vehicle_type,
            biome.replace('_', ''),
            'otherides'
        ]
        
        if honorary:
            tags.extend(['honorary', honorary.lower().split('(')[0].strip()])
        
        return tags
    
    def create_honorary_vehicle(self, honoree_name, honoree_org, custom_style=None, custom_traits=None):
        """Create an honorary vehicle like the Garga example"""
        
        vehicle_data = self.generate_otherides_vehicle(
            faction='honorary',
            vehicle_type='buggy',
            biome='miami_swamp',
            style=custom_style or 'rough_cool_tattoo',
            honorary=f"{honoree_name} ({honoree_org})",
            custom_traits=custom_traits,
            variant=f"{honoree_name} Tribute Vehicle"
        )
        
        if vehicle_data:
            saved_vehicle = self._save_otherides_vehicle(
                vehicle_data, 
                "Honorary_Collection", 
                subfolder="Honoraries"
            )
            return saved_vehicle
        
        return None
    
    def _save_otherides_vehicle(self, vehicle_data, batch_name, subfolder=None):
        """Save vehicle with OTHERIDES metadata structure"""
        
        # Download image
        image_data = self._download_image(vehicle_data['image_url'])
        if not image_data:
            return None
        
        # Create filename and metadata
        file_name = f"{vehicle_data['image_id']}.png"
        
        if subfolder:
            file_path = f"/Otherides_Moodboards/{subfolder}/"
        else:
            faction_folder = vehicle_data['faction'].replace('_', ' ').title()
            file_path = f"/Otherides_Moodboards/{faction_folder}/"
        
        # Upload to Drive (if available)
        drive_info = None
        if self.drive_service:
            folder_id = self._get_or_create_collection_folder(batch_name, subfolder)
            drive_info = self._upload_to_drive(image_data, file_name, folder_id)
        
        # Create metadata
        metadata = {
            "image_id": vehicle_data['image_id'],
            "faction": vehicle_data['faction'].title(),
            "vehicle_type": vehicle_data['vehicle_type'].title(),
            "variant": vehicle_data['variant'],
            "traits": vehicle_data['traits'],
            "biome": vehicle_data['biome'].replace('_', ' ').title(),
            "style": vehicle_data['style'],
            "camera_view": vehicle_data['camera_view'],
            "lighting": vehicle_data['lighting'],
            "mood": "Dynamic racing spirit",
            "creator": "AI_Generator",
            "generation_date": datetime.now().strftime("%Y-%m-%d"),
            "source_prompt": vehicle_data['prompt'],
            "tags": vehicle_data['tags'],
            "file_name": file_name,
            "file_path": file_path
        }
        
        if vehicle_data.get('honorary'):
            metadata["honorary"] = vehicle_data['honorary']
        
        # Save to database
        vehicle_record = {
            'image_id': vehicle_data['image_id'],
            'faction': vehicle_data['faction'],
            'vehicle_type': vehicle_data['vehicle_type'],
            'variant': vehicle_data['variant'],
            'traits': json.dumps(vehicle_data['traits']),
            'biome': vehicle_data['biome'],
            'style': vehicle_data['style'],
            'camera_view': vehicle_data['camera_view'],
            'lighting': vehicle_data['lighting'],
            'honorary': vehicle_data.get('honorary'),
            'generation_date': datetime.now().strftime("%Y-%m-%d"),
            'source_prompt': vehicle_data['prompt'],
            'tags': json.dumps(vehicle_data['tags']),
            'file_name': file_name,
            'file_path': file_path,
            'drive_id': drive_info['id'] if drive_info else None,
            'drive_link': drive_info['webViewLink'] if drive_info else None,
            'collection_batch': batch_name,
            'created_at': datetime.now().isoformat(),
            'image_hash': hashlib.md5(image_data.getvalue()).hexdigest()
        }
        
        vehicle_id = self._save_vehicle_record(vehicle_record)
        
        return {
            'id': vehicle_id,
            'metadata': metadata,
            'drive_link': drive_info['webViewLink'] if drive_info else None,
            'file_name': file_name
        }
    
    def _download_image(self, image_url):
        """Download image from URL"""
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            return io.BytesIO(response.content)
        except Exception as e:
            print(f"Error downloading image: {e}")
            return None
    
    def _upload_to_drive(self, image_data, filename, folder_id):
        """Upload image to Google Drive"""
        if not self.drive_service:
            return None
            
        try:
            file_metadata = {
                'name': filename,
                'parents': [folder_id] if folder_id else []
            }
            
            media = MediaIoBaseUpload(image_data, mimetype='image/png', resumable=True)
            
            file = self.drive_service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id,webViewLink,webContentLink'
            ).execute()
            
            return file
            
        except Exception as e:
            print(f"Error uploading to Drive: {e}")
            return None
    
    def _get_or_create_collection_folder(self, batch_name, subfolder=None):
        """Create organized folder structure"""
        if not self.drive_service:
            return None
            
        try:
            main_folder_id = self._get_or_create_folder("OTHERIDES_Collection")
            
            if subfolder:
                subfolder_id = self._get_or_create_folder(subfolder, main_folder_id)
                return subfolder_id
            else:
                batch_folder_id = self._get_or_create_folder(batch_name, main_folder_id)
                return batch_folder_id
            
        except Exception as e:
            print(f"Error creating folder structure: {e}")
            return None
    
    def _get_or_create_folder(self, folder_name, parent_id=None):
        """Get existing or create new folder"""
        if not self.drive_service:
            return None
            
        try:
            search_query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'"
            if parent_id:
                search_query += f" and '{parent_id}' in parents"
            
            results = self.drive_service.files().list(
                q=search_query,
                fields="files(id, name)"
            ).execute()
            
            folders = results.get('files', [])
            if folders:
                return folders[0]['id']
        except Exception:
            pass
        
        # Create new folder
        try:
            file_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            if parent_id:
                file_metadata['parents'] = [parent_id]
            
            folder = self.drive_service.files().create(
                body=file_metadata,
                fields='id'
            ).execute()
            
            return folder.get('id')
            
        except Exception as e:
            print(f"Error creating folder {folder_name}: {e}")
            return None
    
    def _save_vehicle_record(self, record):
        """Save vehicle metadata to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        columns = ', '.join(record.keys())
        placeholders = ', '.join(['?' for _ in record])
        
        cursor.execute(
            f"INSERT INTO otherides_vehicles ({columns}) VALUES ({placeholders})",
            list(record.values())
        )
        
        vehicle_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return vehicle_id

def main():
    """Example usage"""
    generator = OtheridesAssetGenerator()
    
    print("🏁 OTHERIDES Asset Generator")
    print("="*50)
    
    # Create an Honorary vehicle
    print("Creating Honorary Vehicle...")
    garga_vehicle = generator.create_honorary_vehicle(
        honoree_name="Garga",
        honoree_org="Yuga Labs",
        custom_style="rough_cool_tattoo",
        custom_traits=["leopard_skin_pattern", "tattoo_body_art", "grill_smirk", "dual_headlight_eyes"]
    )
    
    if garga_vehicle:
        print(f"✅ Created Honorary: {garga_vehicle['metadata']['variant']}")
        print(f"📁 File: {garga_vehicle['file_name']}")
        if garga_vehicle['drive_link']:
            print(f"🔗 Drive: {garga_vehicle['drive_link']}")
    
    # Create faction vehicles with real Otherside biomes
    print("\nCreating Faction Vehicles...")
    faction_vehicles = []
    
    biome_examples = ['molten', 'crystal', 'shadow', 'jungle', 'chaos']
    
    for i, faction in enumerate(['amalfi', 'raven_coats', 'scion', 'kerr_org', 'apostates']):
        if faction not in generator.racing_factions:
            print(f"⚠️ Skipping {faction} - not found in faction data")
            continue
            
        vehicle_data = generator.generate_otherides_vehicle(
            faction=faction,
            biome=biome_examples[i % len(biome_examples)],
            style='noble_refined' if faction == 'amalfi' 
                  else 'mystical_ritual' if faction == 'apostates'
                  else 'sleek_corporate' if faction == 'scion'
                  else 'organic_bio' if faction == 'kerr_org'
                  else 'brutalist_industrial'
        )
        
        if vehicle_data:
            saved_vehicle = generator._save_otherides_vehicle(
                vehicle_data,
                "Genesis_Alpha_Collection"
            )
            if saved_vehicle:
                faction_vehicles.append(saved_vehicle)
                biome_name = biome_examples[i % len(biome_examples)].title()
                print(f"✅ {faction.title()}: {saved_vehicle['metadata']['variant']} in {biome_name}")
    
    print(f"\n🎉 Generated {len(faction_vehicles) + (1 if garga_vehicle else 0)} vehicles")
    print("📊 All vehicles saved with OTHERIDES metadata structure")
    print("🌍 Using real Otherside metaverse biomes!")
    print("🔗 Ready for 3D pipeline integration!")

if __name__ == "__main__":
    main()
