from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
import logging
import os
import glob
from datetime import datetime
from src.graph import run_proposal_generation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins     = ["*"],
    allow_credentials = True ,
    allow_methods     = ["*"],
    allow_headers     = ["*"],
)


class GenerateProposalRequest(BaseModel):
    questionnaire: str
    user_prompt: Optional[str] = ""


@app.post("/generate-proposal")
async def generate_proposal(request: GenerateProposalRequest):
    try:
        logger.info("=" * 80)
        logger.info("REQUEST RECEIVED")
        logger.info("=" * 80)

        logger.info("QUESTIONNAIRE:")
        logger.info(request.questionnaire)

        logger.info("-" * 80)

        logger.info("USER PROMPT:")
        logger.info(request.user_prompt)

        # Prepare the questionnaire data
        questionnaire = {
            "questionnaire": request.questionnaire,
            "user_prompt": request.user_prompt
        }

        # Run the proposal generation
        final_state = run_proposal_generation(questionnaire)

        logger.info("=" * 80)
        logger.info("PROPOSAL GENERATION COMPLETE")
        logger.info("=" * 80)

        # Find the generated DOCX file
        docx_files = glob.glob("./x_results/Proposal*.docx")
        
        if not docx_files:
            # Try alternative patterns
            docx_files = glob.glob("./x_results/*.docx")
            
        if not docx_files:
            # Check if proposal has word_path
            proposal = final_state.get("proposal", {})
            word_path = proposal.get("word_path")
            if word_path and os.path.exists(word_path):
                docx_files = [word_path]
        
        if not docx_files:
            logger.warning("No DOCX file found in x_results directory")
            # Return JSON response with error info
            return {
                "success": False,
                "error": "No DOCX file generated",
                "final_state": final_state
            }
        
        # Get the most recent DOCX file
        latest_docx = max(docx_files, key=os.path.getctime)
        logger.info(f"Found DOCX file: {latest_docx}")
        
        # Return the file for download
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"proposal_{timestamp}.docx"
        
        return FileResponse(
            path=latest_docx,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename=filename
        )

    except Exception as e:
        logger.error(f"Error generating proposal: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health():
    return {"status": "ok", "timestamp": datetime.now().isoformat()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8008,
        reload=True
    )