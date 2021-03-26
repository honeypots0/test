"use strict";

/*
This is the page for which we want to rewrite the User-Agent header.
*/
var targetPage = "*://*/*";

/*
Set UA string to Opera 12
*/
var ua = "https://www.youtube.com";
var ua2 = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
/*
Rewrite the User-Agent header to "ua".
*/
function rewriteUserAgentHeader(e) {
  for (var header of e.requestHeaders) {
    if (header.name === "User-Agent") {
      header.value = ua2;
      header.name = "Referer";
      header.value = ua;
    }
  }
  return {requestHeaders: e.requestHeaders};
}

/*
Add rewriteUserAgentHeader as a listener to onBeforeSendHeaders,
only for the target page.

Make it "blocking" so we can modify the headers.
*/
browser.webRequest.onBeforeSendHeaders.addListener(
  rewriteUserAgentHeader,
  {urls: [targetPage]},
  ["blocking", "requestHeaders"]
);
