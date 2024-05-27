def responseIntepretation(response):
    if len(response) > 4:
        return "Unknown"
    if "Y" in response:
        return "Yes"
    if "N" in response:
        return "No"
    else:
      return 'Error'
    
def getResponse(model, prompt):
    if model["rawResults"] == False:
        response = model["LLM"].invoke(prompt).content
    else:
        response = model["LLM"].invoke(prompt)
    return response