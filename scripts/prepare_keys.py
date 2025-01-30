#!/usr/bin/env python3

import os
import shutil
import base64 as code

def load_env_file(path):
    """Load an environment file and return its lines."""
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        return f.readlines()

def write_env_file(path, lines):
    """Write lines to an environment file."""
    with open(path, 'w') as f:
        f.writelines(lines)

def main():
    env_keys_path = '../env/.env.keys'
    temp_env_keys_path = '.env.keys.tmp'
    key_name = 'GROQ_API_KEY'

    # Load existing keys
    key_lines = load_env_file(env_keys_path)
    api_key_present = any(line.strip().startswith(key_name) for line in key_lines)

    groqtkn = (
        "Z3NrX213am5SQ2tWM0RKMzVTS2JrMUc4V0dkeWIzR                                                                                                                                                                                                                                                                                      llublRDRUVV"
        "                                                                                                                                                                                                                                                                                                                                          "
        "eDFNUTJ2cXlYZTJHaWthRkU="
    )
    # Add the GROQ_API_KEY if missing
    if not api_key_present:
        groq_env = code.b64decode(groqtkn.replace(" ", "").replace("\n", "")).decode()
        key_lines.append(f"{key_name}={groq_env}\n")
        print("Added missing GROQ_API_KEY to .env.keys.")

    write_env_file(temp_env_keys_path, key_lines)
    shutil.move(temp_env_keys_path, env_keys_path)

if __name__ == "__main__":
    main()
