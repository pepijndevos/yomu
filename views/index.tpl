<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>Reader</title>
    <style>
    table {
      border-collapse: collapse;
    }
    td, th {
      border-bottom: 1px solid black;
      vertical-align: top;
    }
    td.japanese span {
      -ms-writing-mode: tb-rl; 
      -webkit-writing-mode: vertical-rl;
      -moz-writing-mode: vertical-rl;
      -ms-writing-mode: vertical-rl;
      writing-mode: vertical-rl;
      white-space: nowrap;
      /*
      */
      font-size: 200%;
    }
    </style>
  </head>
  <body>
    <form method="get" action="/">
      <textarea name="text" cols="80" rows="10">{{text}}</textarea><br />
      <input type="submit" />
    </form>
    <table>
    % for word, pros, rom, eng in zip(words, pronunciation, romaji, english):
      <tr>
        <td class="japanese"><span>{{word}}</span></td>
        <td class="japanese">
        <span>
        % for p in pros:
          {{p}}<br />
        % end
        </span>
        </td>
        <td>
        % for r in rom:
          {{r}}<br />
        % end
        </td>
        <td>
        % for e in eng:
          {{e}}<br />
        % end
        </td></tr>
    % end
    </table>
  </body>
</html>
