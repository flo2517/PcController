const path = require("path");

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

const downloadFile = (req, res) => {
  let file = req.params.file;
  if(file === 'win') {
    res.download(path.join(__dirname, '../../../public/downloads/Premote_win.rar'));
  } else if(file === 'mac') {
    res.download('./public/downloads/mac.exe');
  } else if(file === 'linux') {
    res.download(path.join(__dirname, '../../../public/downloads/Premote_linux.rar'));
  } else if(file === 'android') {
    res.download(path.join(__dirname, '../../../public/downloads/android.apk'));
  } else {
    res.status(404).render('pages/404', {
      title: '404',
      page: '404'
    });
  }
};

module.exports = {
  home,
  about,
  download,
  downloadFile
};