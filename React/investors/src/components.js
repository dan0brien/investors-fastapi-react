import {formatNumber} from './helpers'

export function SummaryTable({investorSummary, handleRowClick}) {
    return (
    <table className='table table-striped table-bordered table-hover'>
        <thead>
          <tr>
            <th>Investor Name</th>
            <th>Investory Type</th>
            <th>Total Commitment Amount</th>
            <th>Currency</th>
          </tr>
        </thead>
        <tbody>
          {investorSummary.map((investorSum) =>(
            <tr key ={investorSum.investor_name} onClick={() => handleRowClick(investorSum.investor_name)}>
              <td>{investorSum.investor_name}</td>
              <td>{investorSum.investory_type}</td>
              <td>{formatNumber(investorSum.total_commitment_amount)}</td>
              <td>{investorSum.commitment_currency}</td>
            </tr>
          ))}
        </tbody>
      </table>
    );
}

export function InvestorTable({filteredData, handleFilterChange}) {
    const total_sum = filteredData.reduce ((sum, investor) =>sum + investor.commitment_amount, 0)
    return(
        <div>
            <div style={{ display: 'flex', justifyContent: 'space-evenly' }}>
                <h2>Total Value: {formatNumber(total_sum)}</h2>
            </div>
            <FilterButtons handleFilterChange={handleFilterChange}>
                  </FilterButtons>
            <table className='table table-striped table-bordered table-hover'>
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Commitment Asset Class</th>
                    <th>Commitment Amount</th>
                    <th>Currency</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredData.map((investor) =>(
                    <tr key ={investor.id}>
                      <td>{investor.id}</td>
                      <td>{investor.commitment_asset_class}</td>
                      <td>{formatNumber(investor.commitment_amount)}</td>
                      <td>{investor.commitment_currency}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
    )
}

export function FilterButtons({handleFilterChange}) {
    return (
        <div style={{ display: 'flex', justifyContent: 'space-evenly' }}>
          <h3>Asset Class:</h3>
          <button onClick={() => handleFilterChange("")}> 
          All
          </button>
          <button onClick={() => handleFilterChange("Hedge Funds")}>
          Hedge Funds
          </button>
          <button onClick={() => handleFilterChange("Private Equity")}>
          Private Equity
          </button>
          <button onClick={() => handleFilterChange("Private Debt")}>
          Private Debt
          </button>
          <button onClick={() => handleFilterChange("Real Estate")}>
          Real Estate
          </button>
          <button onClick={() => handleFilterChange("Infrastructure")}>
          Infrastructure
          </button>
          <button onClick={() => handleFilterChange("Natural Resources")}>
          Natural Resources
          </button>
        </div>
    )
}