from basic_pitch.inference import predict, Model
from basic_pitch import ICASSP_2022_MODEL_PATH
import json

def lambda_handler(event, context):
  try: 
    #need to download a wav file from some external source and name it #local_wav
    local_results_file = "/tmp/results.mid"
    model_output, midi_data, note_events = predict(local_wav, basic_pitch_model)
    midi_data.write(local_results_file)
    #consider uploaindg this file to s3 or some external source.
    #or return it in the body
    return {
      'statusCode': 200,
      'body': json.dumps("success")
    }
    
  #
  # on an error, try to upload error message to S3:
  #
  except Exception as err:
    print("**ERROR**")
    print(str(err))
    return {
      'statusCode': 400,
      'body': json.dumps(str(err))
    }
