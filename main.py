from fastapi import FastAPI
import models
app = FastAPI(
    title='Form Getter'
)
@app.post('/get_form/', response_model=dict)
async def getForm(inputData: models.InputModel):
    inputDict = dict(subString.split("=") for subString in inputData.input.split("&"))
    return models.getAnswer(inputDict)
