from pydantic import BaseModel, field_validator

class Config(BaseModel):
    # 配置apikey
    ai_topia_api_key: str = "topia_d92af2ce76994f"
    ai_topia_api_secret: str = "a4407c568ff543e08a5151d0b89a55f0"

    # 角色体ID
    ai_topia_role_id: str ="2472878"

    # 插件回复优先级：数值越小优先级越高，最小为1
    ai_topia_priority: int = 20

    
    
