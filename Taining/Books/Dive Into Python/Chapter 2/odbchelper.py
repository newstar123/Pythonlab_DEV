#coding:utf8

def buildConnectionString(params):
	"""Build a connection string from a dictionary of parameters.

	Returns string."""
	return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
	myParams = {"server":"mpilgrim", \
				"database":"master", \
				"uid":"sa", \
				"pwd":"secret" \
				}

	print buildConnectionString(myParams)



"""
运行结果：
pwd=secret;database=master;uid=sa;server=mpilgrim
"""