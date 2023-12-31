import re
import argparse

def check_sql_standards(sql_query):
    # Check for UPPERCASE SQL keywords
    uppercase_keywords = re.findall(r'\b(?:SELECT|FROM|WHERE|AND|OR|JOIN|LEFT JOIN|RIGHT JOIN|INNER JOIN|GROUP BY|ORDER BY|CREATE|INSERT INTO|UPDATE|DELETE FROM|BEGIN TRANSACTION|COMMIT)\b', sql_query, flags=re.IGNORECASE)
    
    # Check for indentation
    indentation_check = re.search(r'^\s*SELECT', sql_query, re.MULTILINE)
    
    # Check for table and column aliases
    alias_check = re.findall(r'\b(?:\w+)\s+AS\s+(\w+)', sql_query, re.IGNORECASE)
    
    # Check for consistent capitalization in identifiers
    consistent_capitalization = re.findall(r'\b(?:[A-Z_]\w*|"[^"]+")\b', sql_query)
    
    # Check for comments
    comment_check = re.findall(r'--.*$', sql_query, re.MULTILINE)
    
    # Check for wildcard usage
    wildcard_check = re.search(r'\bSELECT\s+\*\s+FROM\b', sql_query, re.IGNORECASE)
    
    # Check for keywords used as identifiers
    reserved_word_check = re.findall(r'\b(?:SELECT|FROM|WHERE|AND|OR|JOIN|LEFT JOIN|RIGHT JOIN|INNER JOIN|GROUP BY|ORDER BY|CREATE|INSERT INTO|UPDATE|DELETE FROM|BEGIN TRANSACTION|COMMIT)\b', sql_query, flags=re.IGNORECASE)
    
    # Print results
    print("Uppercase Keywords:", uppercase_keywords)
    print("Indentation Check:", "Passed" if indentation_check else "Failed")
    print("Alias Naming:", alias_check)
    print("Consistent Capitalization:", consistent_capitalization)
    print("Comments:", comment_check)
    print("Wildcard Usage:", "Avoided" if not wildcard_check else "Used")
    
    print("Reserved Words as Identifiers:", reserved_word_check)


def extract_queries_from_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        # Split queries based on semicolons
        queries = re.split(r';\s*\n', file_content)
        # Remove empty strings
        queries = [query.strip() for query in queries if query.strip()]
    return queries

def main(file_path):
    queries = extract_queries_from_file(file_path)
    
    for i, query in enumerate(queries, start=1):
        print(f"\nChecking standards for Query {i}:")
        check_sql_standards(query)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check SQL standards in a file")
    parser.add_argument("file_path", help="Path to the SQL file")

    args = parser.parse_args()
    main(args.file_path)

'''/home/adithya/Documents/SQL Code Quality Check/sampleQuery.sql'''