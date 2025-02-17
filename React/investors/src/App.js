import React, {useState, useEffect} from 'react'
import api from './api'
import {InvestorTable, SummaryTable} from './components'

const App = () => {
  const [investorSummary, setInvestorSummary] = useState([]);
  const [investor, setInvestor] = useState([]);
  const [filterCriteria, setFilterCriteria] = useState('')
  const [showSummary, setShowSummary] = useState(true)
  const [currentInvestor, setCurrentInvestor] = useState('')

  const handleReturnClick = () => {
    setCurrentInvestor('');
    setFilterCriteria('');
    setShowSummary(true);
  }

  const handleRowClick = (investor_name) => {
    setCurrentInvestor(investor_name);
    fetchInvestor(investor_name);
    setShowSummary(false);
  };

  const handleFilterChange = (filter) => {
    setFilterCriteria(filter);
  };
  
  const fetchInvestorsSummary = async () => {
    const response = await api.get('/investors_summary/');
    setInvestorSummary(response.data)
  };

  const filteredData = investor.filter((commitment) =>
    filterCriteria === '' || commitment.commitment_asset_class === filterCriteria
  );
  
  const fetchInvestor = async (investor) => {
    const url = '/investor/'+ investor + '/'
    const response = await api.get(url);
    setInvestor(response.data)
  };

  useEffect(() => {
    fetchInvestorsSummary();
  }, []);


  return (
  <div>
    {!showSummary && <div>
      <h1>{currentInvestor}</h1>
      <button   onClick={handleReturnClick}> 
        Return to Summary
      </button>
      <InvestorTable filteredData={filteredData} handleFilterChange={handleFilterChange}>
      </InvestorTable>
    </div>}
  
    {showSummary && <div>
      <h1>Investor Summary</h1>
      <SummaryTable investorSummary={investorSummary} handleRowClick={handleRowClick}>
      </SummaryTable>
    </div>}
  </div>
  )
}
export default App;
