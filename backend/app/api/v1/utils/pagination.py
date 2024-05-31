def paginate(query, skip: int = 0, limit: int = 10):
    return query.offset(skip).limit(limit).all()