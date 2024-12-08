const handleSearch = async () => {
  const response = await fetch(`http://localhost:5000/results/${rollNo}`);
  const data = await response.json();
  setResult(data);
};
