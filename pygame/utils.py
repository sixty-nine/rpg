def ensure(cond, msg):
	if not cond: raise ValueError(msg)
