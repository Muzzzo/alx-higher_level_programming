#!/usr/bin/env node
const fs = require('fs');

// Check if the file path argument is provided
if (process.argv.length < 3) {
  console.error('Usage: node read_file.js <file_path>');
  process.exit(1);
}

// Extract the file path from the command-line arguments
const filePath = process.argv[2];

// Check if the file exists
if (!fs.existsSync(filePath)) {
  console.error(`File '${filePath}' does not exist.`);
  process.exit(1);
}

// Check if the file is readable
fs.access(filePath, fs.constants.R_OK, (err) => {
  if (err) {
    console.error(`File '${filePath}' is not accessible: ${err}`);
    process.exit(1);
  }

  // Read the content of the file
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
});
