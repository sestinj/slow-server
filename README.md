`main.py` contains an OpenAI-compatible FastAPI server that can be used to check whether a connection will timeout. It will stream integers from 0 to 3600, one per second. At one hour, it stops.

To run the server:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

To test the server with Continue, add a model to your `"models"` array in `config.json` like this:

```json
{
  "models": [
    {
      "title": "Slow Server",
      "provider": "openai",
      "model": "<can be anything>",
      "apiBase": "http://localhost:8000"
    }
  ]
}
```

Once you select the model and enter a message, it will start counting.
