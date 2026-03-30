#!/usr/bin/env python3
"""
Script to remove specific keys from config.json files in the outputs directory.
Removes: resize_shape, crop_ratio, compile_model, compile_mode
"""

import json
import os
from pathlib import Path

def clean_config_files(root_dir):
    """Find and clean all config.json files in the directory tree."""
    keys_to_remove = {'resize_shape', 'crop_ratio', 'compile_model', 'compile_mode'}
    
    config_files = list(Path(root_dir).rglob('config.json'))
    
    if not config_files:
        print(f"No config.json files found in {root_dir}")
        return
    
    print(f"Found {len(config_files)} config.json files")
    
    for config_path in config_files:
        try:
            # Load the JSON file
            with open(config_path, 'r') as f:
                config = json.load(f)
            
            # Check if any keys to remove exist
            found_keys = [key for key in keys_to_remove if key in config]
            
            if found_keys:
                # Remove the keys
                for key in found_keys:
                    del config[key]
                
                # Write back to file with proper formatting
                with open(config_path, 'w') as f:
                    json.dump(config, f, indent=4)
                
                print(f"✓ Cleaned {config_path}")
                print(f"  Removed: {', '.join(found_keys)}")
            else:
                print(f"- No changes needed: {config_path}")
                
        except json.JSONDecodeError as e:
            print(f"✗ Error parsing JSON in {config_path}: {e}")
        except Exception as e:
            print(f"✗ Error processing {config_path}: {e}")

if __name__ == '__main__':
    outputs_dir = os.path.expanduser('~/humjie/lerobot_so101_bimanual/outputs')
    
    if os.path.exists(outputs_dir):
        clean_config_files(outputs_dir)
    else:
        print(f"Directory not found: {outputs_dir}")
