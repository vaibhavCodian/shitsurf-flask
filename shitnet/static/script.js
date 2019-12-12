function truncateText(selector, maxLength) {
    var element = document.getElementById(selector),
        truncated = element.innerText;

    if (truncated.length > maxLength) {
        truncated = truncated.substr(0,maxLength) + '...';
    }
    return truncated;
}
//You can then call the function with something like what i have below.
document.getElementById('content').innerText = truncateText('content', 107);
