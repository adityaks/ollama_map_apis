import requests
import argparse
import json
import sys

def print_response(title, response):
    print(f"\n=== {title} ===")
    print(f"Status: {response.status_code}")
    try:
        print("Response:", json.dumps(response.json(), indent=2))
    except Exception:
        print("Response Text:", response.text)

def main():
    print("--== [ Enumerating Cofnigured LLMs on the Ollama Server ] ==--\n")
    parser = argparse.ArgumentParser(
        description="Send HTTP requests to all Ollama API endpoints.",
        usage="python %(prog)s --ip <IP_ADDRESS> --port <PORT>\n\nExample:\n  python %(prog)s --ip 127.0.0.1 --port 11434",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--ip", type=str, required=True, help="Ollama server IP address")
    parser.add_argument("--port", type=int, required=True, help="Ollama server port")

    # If no args provided, print help and exit
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    base_url = f"http://{args.ip}:{args.port}"

    # 1. /
    resp = requests.get(f"{base_url}/")
    print_response("GET /api/tags", resp)

    # 1. /api/
    resp = requests.get(f"{base_url}/api/")
    print_response("GET /api/tags", resp)

    # 1. /api/tags
    resp = requests.get(f"{base_url}/api/tags")
    print_response("GET /api/tags", resp)


if __name__ == "__main__":
    main()

