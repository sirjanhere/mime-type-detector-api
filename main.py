from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

app = FastAPI()

# Allow all origins (for testing/submission platforms)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_methods=["*"],  # allow all HTTP methods
    allow_headers=["*"],  # allow all headers
)

class Attachment(BaseModel):
    url: str

class FileRequest(BaseModel):
    attachments: Attachment

@app.post("/file")
def detect_mime(data: FileRequest):
    data_uri = data.attachments.url

    # Validate Data URI
    match = re.match(r'data:(.*?);base64,', data_uri)
    if not match:
        return {"type": "unknown"}
    
    mime_type = match.group(1)  # e.g., 'image/png'

    # Map main type
    if mime_type.startswith("image/"):
        return {"type": "image"}
    elif mime_type.startswith("text/"):
        return {"type": "text"}
    elif mime_type.startswith("application/"):
        return {"type": "application"}
    else:
        return {"type": "unknown"}
