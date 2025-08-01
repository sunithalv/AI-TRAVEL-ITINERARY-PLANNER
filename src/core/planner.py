from langchain_core.messages import HumanMessage,AIMessage
from src.chains.itinerary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages=[]
        self.city=""
        self.interests=[]
        self.itineary=""

        logger.info("Initialized TravelPlanner instance")

    def set_city(self,city:str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("City set successfully")
        except Exception as e:
            logger.error(f"Error while setting city : {e}")
            raise CustomException("Failed to set city" , e)
        
    def set_interests(self,interests_str:str):
        try:
            self.interests = [i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interest also set successfully..")
        except Exception as e:
            logger.error(f"Error while setting interests : {e}")
            raise CustomException("Failed to set interest" , e)
        
    def create_itinerary(self):
        try:
            logger.info(f"Generating create_itinerary for {self.city} and for interests : {self.interests}")
            itinerary = generate_itinerary(self.city,self.interests)
            self.itinerary = itinerary
            self.messages.append(AIMessage(content=itinerary))
            logger.info("Itinerary generated successfully..")
            return itinerary
        except Exception as e:
            logger.error(f"Error while creating itinerary : {e}")
            raise CustomException("Failed to create itinerary" , e)
