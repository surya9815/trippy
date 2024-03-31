import os, redis,json
from django.conf import settings
from redis.commands.json.path import Path

class RedisUtils():
    def __init__(self, host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), password=os.environ.get('REDIS_PASSWORD')):
        self.host = host
        self.port = port
        self.password = password
        self.redis = redis.StrictRedis(
            host=self.host,
            port=self.port,
            password=self.password,
            decode_responses=True
        )

    # ------------------------------------ GENERIC ------------------------------------
    def is_redis_available(self):
        try:
            return self.redis.ping()
        except (redis.exceptions.ConnectionError, ConnectionRefusedError):
            print("Redis connection error!")
            return False
        except Exception as e:
            print("Error in the is_redis_available function", e)
            return False
    def run_raw_redis_query(self,redis_command):
        """ 
        If there is a Custom Command you want to execute then use this
        """
        try:
            result = self.redis.execute_command(redis_command)
            return result
        except redis.exceptions.ResponseError as e:
            print(f"Error Calling Redis: {str(e)}")
    
    def check_key_exists_redis(self,key_name):
        """
        Check if Key Exists in Redis otherwise return
        """
        try:
            result = self.redis.exists(key_name)
            if result:
                return True
            return False
        except redis.exceptions.ResponseError as e:
            print(f"Checking Key in Redis Failed: {str(e)}")
    
    def check_memory_usage(self,key_name="all"):
        try:
            if key_name == "all":
                memory_stats = self.run_raw_redis_query('MEMORY STATS')
            else:
                memory_stats = self.run_raw_redis_query(f'MEMORY USAGE {key_name}')
                if isinstance(memory_stats,int):
                    memory_stats = memory_stats / 1024
            return memory_stats
        except redis.exceptions.ResponseError as e:
            print(f"Checking Memory in Redis Failed: {str(e)}")

    # ------------------------------------ JSON Redis ------------------------------------
    def json_set_value(self,key_name,key_value,key_path='.',expiry=None):
        """
        Set the JSON value at key ``name`` under the ``path`` to ``obj``.
        """
        try:
            key_path=Path(f'{key_path}')
            result = self.redis.json().set(key_name,key_path,key_value)
            if result:
                if expiry:
                    self.redis.expire(key_name, expiry)
                return result
            else:
                return False
        except redis.exceptions.ResponseError as e:
            print(f"Error Setting JSON Data: {str(e)}")
    
    def json_get_value(self,key_name,key_path = '.'):
        """
        Get the object stored as a JSON value at key ``name``.
        """
        try:
            key_path = Path(f'{key_path}')
            result = self.redis.json().get(key_name,key_path)
            return result
        except redis.exceptions.ResponseError as e:
            print(f"Error Getting JSON Data:  {str(e)}")
    
    def json_del_value(self,key_name,key_path='.'):
        """
        Delete the JSON value stored at key ``key`` under ``path``. 
        Can Delete Nested Values
        Returns as True or False : 1 for Sucess  
        """
        try:
            key_path = Path(f'{key_path}')
            result = self.redis.json().delete(key_name,key_path)
            return result == 1
        except redis.exceptions.ResponseError as e:
            print(f"Error Deleting JSON Data:  {str(e)}")
    
    def json_append_value(self,key_name, data_to_append, key_path='.'):
        """Append the objects ``args`` to the array under the
        ``path` in key ``name``.
        Returns the index + 1  of the item entered :  You can Use as the count of items inside the Key specified 
        """
        try:
            key_path = Path(f'{key_path}')
            result = self.redis.json().arrappend(key_name, key_path, data_to_append)
            return result
        except redis.exceptions.ResponseError as e:
            print(f"Error Appending JSON Data:  {str(e)}")
    
    def json_update_value(self,key_name,key_value,key_path='.'):
        """
        Update or set new JSON value at key ``name`` under the ``path`` to ``obj``.
        """
        try:
            key_path=Path(f'{key_path}')
            result = self.redis.json().set(key_name,key_path,key_value)
            return result
        except redis.exceptions.ResponseError as e:
            print(f"Error Updating JSON Data: {str(e)}")

    def json_mem_usage(self, key_name, key_path='.'):
        """Return the memory usage in KB of a value under ``path`` from
        key ``name``.
        """
        try:
            key_path = Path(f'{key_path}')
            result = self.redis.json().debug('MEMORY',key_name ,key_path)
            kb = result / 1024 
            return f'{round(kb,2)} KB'
        except redis.exceptions.ResponseError as e:
            print(f"Error Getting Memory of JSON Data: {str(e)}")


            
    