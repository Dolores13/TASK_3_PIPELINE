import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import project as webapp   

def test_home_page_works():
    client = webapp.app.test_client()   
    response = client.get("/")          
    assert response.status_code == 200  
    assert b"Contest Registration" in response.data 
