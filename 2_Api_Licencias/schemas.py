from pydantic import BaseModel,Field
from datetime import date

# Modelo de Pydantic para los datos de entrada

class Licencia(BaseModel):
    conductor_name: str = Field(None, description="Nombre del conductor")
    tipo: str = Field(None, description="Tipo de licencia, categoria A,B,C")
    fecha_expedicion: date = Field(None, description="Fecha en la que se emitio la licencia")
    numero: str = Field(None, description="Numero de la licencia")

class Vigencia(BaseModel):
    licencia_id: int = Field(None, description="ID de la licencia de la tabla licencia")
    fecha_ini_vig: date = Field(None, description="Fecha en la que inicia la vigencia de la licencia")
    fecha_fin_vig: date = Field(None, description="Fecha en la que termina la vigencia de la licencia")

class Estado(BaseModel):
    vigencia_id: int = Field(None, description="ID de la vigencia de la tabla vigencia")
    estado: str = Field(None, description="Estado de la vigencia")
    fecha_estado: date = Field(None, description="Fecha del estado de la vigencia")

class ConsultaLicencia(BaseModel):
    numero: str = Field(None, description="Numero de la licencia",example="L789012")
    conductor_name: str = Field(None, description="Nombre del conductor")
    tipo: str = Field(None, description="Tipo de licencia, categoria A,B,C")
    fecha_expedicion: date = Field(None, description="Fecha en la que se emitio la licencia")
    fecha_expiracion: date = Field(None, description="Fecha en la que expira la licencia")
    estado: str = Field(None, description="Estado de la vigencia")
    fecha_estado: str = Field(None, description="Fecha del estado de la vigencia")

class LicenciaUpdate(BaseModel):
    conductor_name: str = Field(None, description="Nombre del conductor")
    tipo: str = Field(None, description="Tipo de licencia, categoria A,B,C")
    fecha_expedicion: date = Field(None, description="Fecha en la que se emitio la licencia")

class VigenciaUpdate(BaseModel):
    fecha_ini_vig: date = Field(None, description="Fecha en la que inicia la vigencia de la licencia")
    fecha_fin_vig: date = Field(None, description="Fecha en la que termina la vigencia de la licencia")

class EstadoUpdate(BaseModel):
    estado: str = Field(None, description="Estado de la vigencia")
    fecha_estado: date = Field(None, description="Fecha del estado de la vigencia")

class VigenciaResponse(BaseModel):
    id: int = Field(None, description="ID de la vigencia")
    licencia_id: int = Field(None, description="ID de la licencia de la tabla licencia")
    fecha_ini_vig: date = Field(None, description="Fecha en la que inicia la vigencia de la licencia")
    fecha_fin_vig: date = Field(None, description="Fecha en la que termina la vigencia de la licencia")
    class Config:
        from_attributes  = True

class EstadoResponse(BaseModel):
    id: int = Field(None, description="ID del estado")
    vigencia_id: int = Field(None, description="ID de la vigencia de la tabla vigencia")
    estado: str = Field(None, description="Estado de la vigencia")
    fecha_estado: date = Field(None, description="Fecha del estado de la vigencia")
    class Config:
        from_attributes  = True

class LicenciaConFechaExpiracion(BaseModel):
    id: int = Field(None, description="ID de la licencia")
    conductor_name: str = Field(None, description="Nombre del conductor")
    tipo: str = Field(None, description="Tipo de licencia, categoria A,B,C")
    fecha_expedicion: date = Field(None, description="Fecha en la que se emitio la licencia")
    numero: str = Field(None, description="Numero de la licencia")
    fecha_expiracion: date = Field(None, description="Fecha en la que expira la licencia") # Campo nuevo
    class Config:
        from_attributes  = True