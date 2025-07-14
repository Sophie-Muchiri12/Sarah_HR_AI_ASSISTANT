import os
from langflow.main import app
from langflow.services.flow.service import flow_service
import uvicorn

@app.on_event("startup")
async def load_saraha_flow():
    flow_path = "Saraha_HR.json"
    if os.path.exists(flow_path):
        flow_service.load_flow_from_file(flow_path)
    else:
        print(f"Flow file not found: {flow_path}")

if __name__ == "__main__":
    port = int(os.environ.get("LANGFLOW_PORT", 7860))
    uvicorn.run("langflow.main:app", host="0.0.0.0", port=port)
