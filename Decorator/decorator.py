from functools import wraps

def make_doomtag(function):
	@wraps(function)

	# Inner function
	def decorator():
		# Take return value of the function being decorator
		returnValue = function()

		# Add new functionality to the function being decorator
		return "<doom>" + returnValue + "</doom>"

	return decorator

# Apply the decorator
@make_doomtag
def hand_up():
	return "Put your hand up!"

# Check the reuslt
# Result would be: <doom>Put your hand up!</doom>
print hand_up()