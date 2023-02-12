// Octokit.js
// https://github.com/octokit/core.js#readme
const Octokit = require('@octokit/core');
const octokit = new Octokit({
  auth: 'YOUR-TOKEN'
});

async function writeFileToGitHub(fileName, fileContent, commitMessage) {
  const owner = 'OWNER';
  const repo = 'REPO';
  const path = `PATH/${fileName}`;
  const message = commitMessage;
  const committer = {
    name: 'Monalisa Octocat',
    email: 'octocat@github.com'
  };
  const content = Buffer.from(fileContent).toString('base64');

  try {
    const result = await octokit.request('PUT /repos/{owner}/{repo}/contents/{path}', {
      owner,
      repo,
      path,
      message,
      committer,
      content
    });

    console.log(`File ${fileName} was written successfully.`);
    console.log(result);
  } catch (error) {
    console.error(`Failed to write file ${fileName}. Error:`, error);
  }
}

writeFileToGitHub('form_data.csv', 'test content', 'commit message');
