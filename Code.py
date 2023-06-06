import unittest
import json

# Sample response from microservice
response = '''{
   "open_price": 1000,
   "close_price": 1200,
   "open_lot": 0.994,
   "close_lot": 0.994,
   "open_date": "1680586486",
   "close_date": "1683178486",
   "profits_coin": 200,
   "profits_percentage": 0.20,
   "response": {
  "orderId": 145658421578,
       "symbol": "BTCUSDT",
       "status": "NEW",
       "clientOrderId": "cyb_1fff2a2dea13d941",
       "price": "0",
       "avgPrice": "0.00000",
       "origQty": "2.663",
       "executedQty": "0",
       "cumQty": "0",
       "cumQuote": "0",
       "timeInForce": "GTC",
       "type": "MARKET",
       "reduceOnly": false,
       "closePosition": false,
       "side": "BUY",
       "positionSide": "BOTH",
       "stopPrice": "0",
       "workingType": "CONTRACT_PRICE",
       "priceProtect": false,
       "origType": "MARKET",
       "updateTime": 1682942135417
   }
}'''

class Testmicroservice(unittest.TestCase):
    
    
 def test_timeInForce_case_1(self):
    """"timeInForce test Is it in one of the available timeInForce such as "GTC", "IOC", "FOK".""" 
    valid_timeInForce = ["GTC", "IOC", "FOK"]
    response_dict = json.loads(response)
    assert 'response' in response_dict
    assert 'timeInForce' in response_dict['response']
    assert isinstance(response_dict['response']['timeInForce'], str)
    assert response_dict['response']['timeInForce'] in valid_timeInForce
    print('Test case 1 passed.')
    
        
    
 def test_expected_ranges_case_2(self):
    """Test case to check if the values of the fields in the response are within expected ranges."""
    response_dict = json.loads(response)
    assert response_dict['open_price'] > 0
    assert response_dict['close_price'] > 0
    assert 0 <= response_dict['open_lot'] <= 1
    assert 0 <= response_dict['close_lot'] <= 1
    assert response_dict['profits_coin'] >= 0
    assert 0 <= response_dict['profits_percentage'] <= 1
    print('Test case 2 passed.')
    
    
       
    
 def test_response_symbol_case_3(self):
    """Test case to check response symbol case"""
    response_dict = json.loads(response)
    assert response_dict['response']['symbol'] == 'BTCUSDT' 
    print('Test case 3 passed')
    
    
    
    
 def test_price_within_range_case_4(self):
    """Test case to check if the value of the price in the response are within expected ranges between open price and close price""" 
    response_dict = json.loads(response)
    assert 'response' in response_dict
    assert 'price' in response_dict['response']
    assert isinstance(response_dict['response']['price'], str)

    price = float(response_dict['response']['price'])
    open_price = response_dict['open_price']
    close_price = response_dict['close_price']

    assert open_price <= price <= close_price
    print('Test case 4 passed')
    
    
    
 def test_avgPrice_within_range_case_5(self):
    """Test case to check if the value of the avgerage Price in the response are within expected ranges between open price and close price"""  
    response_dict = json.loads(response)
    assert 'response' in response_dict
    assert 'avgPrice' in response_dict['response']
    assert isinstance(response_dict['response']['avgPrice'], str)

    avgPrice = float(response_dict['response']['avgPrice'])
    open_price = response_dict['open_price']
    close_price = response_dict['close_price']

    assert open_price <= avgPrice <= close_price
    print('Test case 5 passed')  
    
 def test_StopPrice_case_6(self):
    """Test case to check if the value of the stop Price in the response are within expected ranges between open price and close price"""  
    response_dict = json.loads(response)
    assert 'response' in response_dict
    assert 'stopPrice' in response_dict['response']
    assert isinstance(response_dict['response']['stopPrice'], str)

    stopPrice = float(response_dict['response']['stopPrice'])
    open_price = response_dict['open_price']
    close_price = response_dict['close_price']

    assert open_price <= stopPrice <= close_price
    print('Test case 6 passed')     
    
    
    
 def test_priceProtect_case_7(self):
    """Test case to check if the price is protect"""   
    response_dict = json.loads(response)
    assert 'response' in response_dict
    assert 'priceProtect' in response_dict['response']
    assert isinstance(response_dict['response']['priceProtect'], bool)
    assert response_dict['response']['priceProtect'] is True
    print('Test case 7 passed') 
    
    
 def test_expected_fields_case_8(self):
    """Test case to check if all the expected fields are present in the response."""
    expected_fields = [
        'open_price',
        'close_price',
        'open_lot',
        'close_lot',
        'open_date',
        'close_date',
        'profits_coin',
        'profits_percentage',
        'response'
    ]
    response_dict = json.loads(response)
    assert all(field in response_dict for field in expected_fields)   
    print('Test case 8 passed')
    
    
 def test_valid_JSON_object_case_9(self):
    """Test case to check if the 'response' field is a valid JSON object."""
    response_dict = json.loads(response)
    assert isinstance(response_dict['response'], dict)
    print('Test case 9 passed')   
    
    
    
 def test_data_types_case_10(self):
    """Test case to check if the data types of the fields in the response are correct."""
    response_dict = json.loads(response)
    assert isinstance(response_dict['open_price'], (int, float))
    assert isinstance(response_dict['close_price'], (int, float))
    assert isinstance(response_dict['open_lot'], (int, float))
    assert isinstance(response_dict['close_lot'], (int, float))
    assert isinstance(response_dict['profits_coin'], (int, float))
    assert isinstance(response_dict['profits_percentage'], (int, float))
    assert isinstance(response_dict['open_date'], str)
    assert isinstance(response_dict['close_date'], str)
    assert response_dict['open_date'].isdigit()
    assert response_dict['close_date'].isdigit()
    print('Test case 10 passed.')   
    
    
if __name__ == "__main__":
    unittest.main()
    