
const home = (req, res) => {
  res.status(200).render('pages/home', {
    title: 'Home',
    page: 'home'
  });
};

const about = (req, res) => {
  res.status(200).render('pages/about', {
    title: 'About',
    page: 'about'
  });
};

const download = (req, res) => {
  res.status(200).render('pages/download', {
    title: 'Download',
    page: 'download'
  });
};

module.exports = {
  home,
  about,
  download
};