# MIME Type Detector API

A simple FastAPI API to detect MIME types from **data URIs**.

The API supports detecting the main type for:

- `image` (e.g., `image/png`, `image/jpeg`)  
- `text` (e.g., `text/plain`, `text/html`)  
- `application` (e.g., `application/json`, `application/pdf`)  
- `unknown` (any other type or invalid data URI)

---

## **Live API URL**

You can access the deployed API here:  
[https://mime-type-detector-api.onrender.com](https://mime-type-detector-api.onrender.com)

---

## **Endpoint**

### POST `/file`

**Request JSON format:**
```json
{
  "attachments": {
    "url": "data:image/png;base64,iVBORw..."
  }
}
```

**Response JSON format:**
```json
{
  "type": "image"
}
```

---

## Run Locally

Clone the repository:

```bash
git clone https://github.com/<your-username>/mime-type-detector-api.git
cd mime-type-detector-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn main:app --reload
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Test with curl

```bash
curl -X POST http://127.0.0.1:8000/file \
-H "Content-Type: application/json" \
-d '{"attachments": {"url": "data:image/png;base64,iVBORw..."}}'
```
