#!/usr/bin/env python3
import argparse
import os
import json
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="CLI Tool")
    parser.add_argument("command", choices=["add", "list", "delete"])
    parser.add_argument("text", nargs="?", help="Text to add")
    parser.add_argument("--id", type=int, help="ID to delete")
    args = parser.parse_args()
    
    data_file = "data.json"
    data = []
    if os.path.exists(data_file):
        with open(data_file) as f:
            data = json.load(f)
    
    if args.command == "add" and args.text:
        data.append({
            "id": len(data) + 1,
            "text": args.text,
            "date": datetime.now().isoformat()
        })
        with open(data_file, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Added: {args.text}")
    
    elif args.command == "list":
        for item in data:
            print(f"{item['id']}. {item['text']} ({item['date'][:10]})")
    
    elif args.command == "delete" and args.id:
        data = [x for x in data if x["id"] != args.id]
        with open(data_file, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Deleted ID: {args.id}")

if __name__ == "__main__":
    main()
