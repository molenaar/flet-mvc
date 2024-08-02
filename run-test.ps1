$currentDir = Get-Location
$testdir = "tests\test_all_controls\"

# Change to the test directory
Set-Location -Path $testdir

# Start the test
flet run

# Change back to the original directory
Set-Location -Path $currentDir