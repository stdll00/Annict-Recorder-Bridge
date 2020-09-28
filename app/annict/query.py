from app.models.common_models import RecordRequest
from datetime import timedelta

"""
response sample


  {
    node: {
      startedAt: "2020-10-02T15:30:00Z",
      annictId: 148195,
      episode: { title: None, number: 1 },
      channel: { name: "TOKYO MX" },
      work: {
        episodesCount: 1,
        seasonName: "AUTUMN",
        seasonYear: 2020,
        title: "ダンジョンに出会いを求めるのは間違っているだろうか III",
        watchersCount: 661,
        media: "TV",
        seriesList: {
          nodes: [
            {
              name: "ダンジョンに出会いを求めるのは間違っているだろうか",
              id: "U2VyaWVzLTM5",
            },
          ],
        },
      },
    },
  },


"""
QUERY_GET_PROGRAM = """
{
  viewer {
    programs(orderBy: {field: STARTED_AT, direction: DESC}) {
      edges {
        node {
          startedAt
          annictId
          episode {
            title
            number
          }
          channel {
            name
          }
          work {
            episodesCount
            seasonName
            seasonYear
            title
            watchersCount
            seasonName
            seasonYear
            title
            media
            episodesCount
            seriesList {
              nodes {
                name
                id
              }
            }
          }
        }
      }
    }
  }
}

"""


def program_parse(node_obj) -> RecordRequest:
    """

    :param node_obj:
    :return:
    """
    obj = node_obj['node']
    try:
        title = obj['work']['seriesList']['nodes'][0]['name']
    except (KeyError, IndexError):
        title = obj['work']['title']

    obj = RecordRequest(
        start_at=obj['startedAt'],
        end_at=obj['startedAt'],
        channel=obj['channel']['name'],
        title=title,
    )
    obj.end_at = obj.start_at + timedelta(minutes=30)
    return obj
