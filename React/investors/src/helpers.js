export function formatNumber(num) {
    if (num >= 1e9) {
        return (num / 1e9).toFixed(1) + 'B'; // Convert to billions
    } else if (num >= 1e6) {
        return (num / 1e6).toFixed(1) + 'M'; // Convert to millions
    } else if (num >= 1e3) {
        return (num / 1e3).toFixed(1) + 'K'; // Convert to thousands
    } else {
        return num.toString(); // Return the number as is if it's less than 1000
    }
}