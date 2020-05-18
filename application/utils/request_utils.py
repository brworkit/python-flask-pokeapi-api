def create_caradhras_header(headers):
    return {"Content-Type": "application/json", "Authorization": headers["Authorization"]}

def extract_file_extension(headers):
    return "." + headers["Content-Type"].split("/", 1)[1]