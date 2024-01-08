import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN", "6727384350:AAG3nZF51JvDaNufOnnIIwbGGiyiiCXP8LQ")
    PYRO_SESSION = getenv("PYRO_SESSION", "BQBLlUGAKtdNjrrYweOhQ6uzmCFdQNufaKxCB12q3P6kajlwn59Vmn3wqRBj9pZZMmbhAdE0jt-CRE3bxCtLnTmikA7x8FkcF_Uap2t7WhS4DbMdjX_HgEhBg8ylNNr2oIwkAEaIHGv1W2aRMBhh2zhDWAZfiuswSQI8cDuL0GABoikIhGUZ6TFdWbpIZz2FYWn6765l-bO1Se2pCIZpfAIRpq3cFabkYv5D_Ucvs6zQnAMyPkKrSVycSsRaKI1gg2tDFyr-PLj7tMe0tdcgdmrmNH4xlEa_JY5V_9kYg38OEYXBLBxrlo8DaJm5KKfST4vR_tvywD3fBWWAbH5gS4LsHBZZ_wA")
    TELEGRAM_APP_HASH= getenv('TELEGRAM_APP_HASH',"4e984ea35f854762dcde906dce426c2d")
    TELEGRAM_APP_ID=int(getenv('TELEGRAM_APP_ID',"6435225"))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
