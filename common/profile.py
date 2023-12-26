from pathlib import Path
import os


class Profile:
    __images_path = None
    
    @staticmethod
    def get_images_path():
        home_path = Path(__file__).parent.parent
        
        images_path = home_path.joinpath("data/images")
        images_path.mkdir(parents=True,exist_ok=True)
        return images_path