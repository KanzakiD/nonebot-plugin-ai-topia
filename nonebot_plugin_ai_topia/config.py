from pydantic import BaseModel, field_validator

class Config(BaseModel):
    # 配置apikey
    ai_topia_api_key: str = "1test"
    ai_topia_api_secret: str = "2test"
    # 插件回复优先级。数值越小优先级越高，最小为1。
    ai_topia_priority: int = 20
    
    

    @field_validator("ai_topia_api_key")
    @classmethod
    def check_key(cls, v: str) -> str:
        if v:
            return v
        raise ValueError("请配置apikey")
    
    @field_validator("ai_topia_api_secret")
    @classmethod
    def check_secret(cls, v: str) -> str:
        if v:
            return v
        raise ValueError("请配置apikey")
    
    @field_validator("ai_topia_priority")
    @classmethod
    def check_priority(cls, v: int) -> int:
        if v >= 1:
            return v
        raise ValueError("优先级最小为1,请重新设置")