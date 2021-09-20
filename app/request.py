from .models import Pitch

def get_pitches(category):
    '''
    Function that gets our pitch list
    '''
    pitch_results = None

    if get_pitch_response['results']:
            pitch_response_list = get_pitch_response['results']
            pitch_results = process_results(pitch_results_list)


    return pitch_results

def process_results(pitch_list):
    '''
    function that processes pitch list and get results in form a list
    Args:
        pitch_list: A list of dictionaries that contain pitch details
    Returns :
        pitch_results: A list of pitch objects
    '''
    
    pitch_results=[]
    for pitch_item in pitch_list:
        id=pitch_item.get('id')
        category=pitch_item.get('category')
        title=pitch_item.get('title')
        description=pitch_item.get('description')

        pitch_object = Pitch(id,category, title, description)
        pitch_results.append(pitch_object)

    return pitch_results

def get_pitch(id):
   
        pitch_object = None
        if pitch_details_response:
            id = pitch_details_response.get('id')
            

            pitch_object = Pitch(id)

        return pitch_object
