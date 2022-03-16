const path = require("path");
const commentService = require("../services/comment.service");

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

const getPagination = (page, size) => {
  const limit = size ? +size : 8;
  const offset = page ? page * limit : 0;
  return { limit, offset };
};

const comments = (req, res) => {
  let service = new commentService();
  const { page, size } = req.query;
  const { limit, offset } = getPagination(page, size);
  const pagePos = page ? page : 0;
  service.getComments(limit, offset)
    .then(comments => {
      // let averageMark = (comments.rows.reduce((sum, comment) => sum + comment.dataValues.note, 0) / comments.rows.length).toFixed(2);
      service.averageRating().then(averageMark => {
        console.log(Math.ceil(comments.count / limit));
        res.status(200).render('pages/comment', {
          title: 'Comments',
          page: 'comments',
          pagePos,
          pageNb: Math.ceil(comments.count / limit),
          size: size ? size : 8,
          comments: comments.rows,
          averageMark: parseFloat(averageMark[0].dataValues.averageRating).toFixed(2)
        });
      }).catch(err => {
        console.log(err);
        res.status(500).render('pages/500', {
          title: '500',
          page: '500'
        });
      });

    })
    .catch(err => {
      console.log(err);
      res.status(500).render('pages/500', {
        title: '500',
        page: '500'
      });
    });

};

const addComment = (req, res) => {
  let service = new commentService();
  const { username, note, comment } = req.body;
  if(!username || !note || !comment) {
    res.status(400).redirect('/comments');
    return;
  }
  console.log(req.body);
  service.addComment({ username, note, comment })
    .then(() => {
      res.redirect('/comments');
    })
    .catch(err => {
      console.log(err);
      res.status(500).render('pages/500', {
        title: '500',
        page: '500'
      });
    });
};

module.exports = {
  home,
  about,
  download,
  downloadFile,
  comments,
  addComment
};