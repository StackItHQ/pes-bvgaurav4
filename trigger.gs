function sending(e) {
  var range = e.range;
  
  var sheetName = range.getSheet().getName();
  var spreadsheetId = SpreadsheetApp.getActiveSpreadsheet().getId();

  var row = range.getRow();
  var col = range.getColumn();
  
  var newValue = e.value;
  
  var oldValue = e.oldValue;  // This might be undefined if not available
  
  Logger.log('Sheet: ' + sheetName);
  Logger.log('Cell edited: ' + range.getA1Notation());
  Logger.log('Old value: ' + oldValue);
  Logger.log('New value: ' + newValue);
  Logger.log('id: '+spreadsheetId)
  Logger.log('x' + row);
  Logger.log('y'+ col);
  var url = 'https://ff6f-101-0-62-251.ngrok-free.app/update'; 
  if(newValue==undefined)
  {
    Logger.log('New value: ' + newValue);
    url='https://ff6f-101-0-62-251.ngrok-free.app/delete';
  }
  var payload = {
    data_index:sheetName,
    x:row,
    y:col,
    data_value:newValue,
    spreadsheet_id:spreadsheetId
  };

  var options = {
    'method' : 'post',
    'contentType': 'application/json',  
    'payload' : JSON.stringify(payload),
    'muteHttpExceptions': true  
  };

  try {
    var response = UrlFetchApp.fetch(url, options);
    Logger.log('Response Code: ' + response.getResponseCode());
    Logger.log('Response Content: ' + response.getContentText());
  } catch (error) {
    Logger.log('Error: ' + error.toString());
  }
}
