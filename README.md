# ollama_map_apis
Assessing the exposed Ollama Server APIs. A basic automated script(tool) to be used for security testing of Ollama APIs

```python
% python3 ollama_map_apis_v1.0.py
--== [ Enumerating Cofnigured LLMs on the Ollama Server ] ==--

usage: python ollama_map_apis_v1.0.py --ip <IP_ADDRESS> --port <PORT>

Example:
  python ollama_map_apis_v1.0.py --ip 127.0.0.1 --port 11434

Send HTTP requests to all Ollama API endpoints.

options:
  -h, --help   show this help message and exit
  --ip IP      Ollama server IP address
  --port PORT  Ollama server port


---- Executing ------


% python3 ollama_map_apis_v1.0.py --ip 78.12.xx.yy --port 50000 
--== [ Enumerating Cofnigured LLMs on the Ollama Server ] ==--


=== GET /api/tags ===
Status: 200
Response Text: Ollama is running

=== GET /api/tags ===
Status: 200
Response Text: "description":"AWX REST API"
FreshRSS API endpoints
Fever compatible API
FreshRSS API endpoints

=== GET /api/tags ===
Status: 200
Response: {
  "models": [
    {
      "name": "llama3:latest",
      "modified_at": "2023-12-07T09:32:18.757212583-08:00",
      "size": 3825819519,
      "digest": "fe938a131f40e6f6d40083c9f0f430a515233eb2edaa6d72eb85c50d64f2300e",
      "details": {
        "format": "gguf",
        "family": "llama",
        "families": null,
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "deepseek-r1:latest",
      "model": "deepseek-r1:latest",
      "modified_at": "2025-03-29T20:18:17.974766226Z",
      "size": 4683075271,
      "digest": "0a8c266910232fd3291e71e5ba1e058cc5af9d411192cf88b6d30e92b6e73163",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "qwen2",
        "families": [
          "qwen2"
        ],
        "parameter_size": "7.6B",
        "quantization_level": "Q4_K_M"
      }
    },
    {
      "name": "llama2:latest",
      "model": "llama2:latest",
      "modified_at": "2024-04-22T20:42:41.0502575+08:00",
      "size": 3826793677,
      "digest": "78e26419b4469263f75331927a00a0284ef6544c1975b826b15abdaef17bb962",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    },
    {
      "name": "openchat:7b",
      "model": "openchat:7b",
      "modified_at": "2025-02-03T17:45:24.5347459+08:00",
      "size": 4109876386,
      "digest": "537a4e03b649d93bf57381199a85f412bfc35912e46db197407740230968e71f",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "7B",
        "quantization_level": "Q4_0"
      }
    }
  ]

```
}
