# from fastapi import Depends, UploadFile
# from typing import List

# from ..service import Service, get_service
# from . import router
# from app.auth.adapters.jwt_service import JWTData
# from app.auth.router.dependencies import parse_jwt_user_data


# @router.post("/shanyraks/{id}/media")
# def upload_file(
#     file: UploadFile, 
#     svc: Service = Depends(get_service), 
#     jwt_data: JWTData = Depends(parse_jwt_user_data)
# ):
#     """
#     file.filename: str - Название файла
#     file.file: BytesIO - Содержимое файла
#     """
#     url = svc.s3_service.upload_file(file.file, file.filename)
    
#     return {"msg": url}

# @router.post("/shanyraks/{id}/media")
# def upload_files(
#     files: List[UploadFile], 
#     svc: Service = Depends(get_service), 
#     jwt_data: JWTData = Depends(parse_jwt_user_data),
# ):
#     """
#     file.filename: str - Название файла
#     file.file: BytesIO - Содержимое файла
#     """
#     result = []
#     for file in files:
#         url = svc.s3_service.upload_file(file.file, file.filename)
#         result.append(url)
    
#     return {"msg": files}