# Parse git log export file into JSON format
import json, sys, os

def parse_record(lines):
	record = {}
	itr = iter(lines)
	for line in itr:
		words = line.split(': ')
		if len(words) == 2:
			name, value = words

			if name == 'MESSAGE':
				# Message could be multi-lines
				message = value.strip()
				while True:
					line = next(itr, None)
					if line == None:
						break
					words = line.split(': ')
					if len(words) > 0 and words[0] == 'FILES':
						name = words[0]
						break
					else:
						message += "\n" + line.strip()
				record['MESSAGE'] = message

			if name == 'FILES':
				# Parse and collect files
				files = []
				while True:
					line = next(itr, None)
					if line == None:
						break
					line = line.strip()
					if line == '':
						break
					files.append(line)
				record['FILES'] = files
				continue
			
			# All other case, we simply keep key: value pair as record
			record[name] = value.strip()
	return record


def parse_git_export_text_to_json(git_export_file, json_output_file):
	print(f"Parsing git export: {git_export_file}")
	records = []
	record_lines = []
	with open(git_export_file, 'r') as fh:
		for line in fh.readlines():
			if line.strip() != '':
				if 'COMMIT: ' in line and len(record_lines) > 0:
					record = parse_record(record_lines)
					if record:
						records.append(record)
					record_lines = []
				record_lines.append(line)
	
	print(f"Writing {len(records)} git commit records to {json_output_file}")
	with open(json_output_file, 'w') as fh:
		fh.write(json.dumps(records, indent=2))

def export_git_lot(output_file):
	cmd = "git log --date=iso-strict --pretty=format:'%nCOMMIT: %H%nAUTHOR: %an <%ae>%nDATE: %ad%nMESSAGE: %f%nFILES: ' --name-only > " + output_file
	print(f"Exporting git log to {output_file}")
	print(f"Command: {cmd}")
	os.system(cmd)

def main():
	output_file = sys.argv[1] if len(sys.argv) > 1 else "commits.json"
	git_export_file = "." + output_file + ".git-export.txt"
	export_git_lot(git_export_file)
	parse_git_export_text_to_json(git_export_file, output_file)
	print(f"Removing {git_export_file}")
	os.remove(git_export_file)
	print(f"Export completed to {output_file}")

if __name__ == "__main__":
	main()
