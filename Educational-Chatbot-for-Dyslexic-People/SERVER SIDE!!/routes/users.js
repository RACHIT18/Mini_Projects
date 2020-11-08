var express = require('express');
var router = express.Router();
const spawn = require('child_process').spawn;
/*default test case, used in case of localhost*/
const ls = spawn('python', ['text_pre.py', 'Where can i findfind nearestmedical shopto center of Arizona']);
 
/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send(req.query.txt);
});

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.log(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`TextPreprocessing process exited with code ${code}`);

  const spawn2=require('child_process').spawn;
const ls2=spawn2('python',['n_gram.py']);

ls2.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls2.stderr.on('data', (data) => {
  console.log(`stderr: ${data}`);
});

ls2.on('close', (code) => {
  console.log(`N-gram process exited with code ${code}`);
});

});




module.exports = router;
