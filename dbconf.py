import importlib
__CURRENT_DB="mysql"
SQL_DIALECT_MODULE="mysql_queries"
profiles={
    "mysql":{
        "_database":"umapython",
        "_host":"localhost",
        "_user":"root",
        "_passwd":'admin123',
        "_admin_passwd":"admin123"
    }
}

def getProvider():
    return importlib.import_module(__CURRENT_DB+"conf")